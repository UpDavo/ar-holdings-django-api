# from rest_framework.response import Response
from rest_framework import status, generics
from django.http.response import JsonResponse
from datetime import date
import json


# Modelos de la base de datos
from ArHoldingsApp.models import (
    CatalogoArticulos,
    FacturacionEncabezado,
)
from ArHoldingsApp.serializers import (
    CatalogoSerializer,
    FacturacionEncabezadoSerializer,
)


# Views for products


class GetProducts(generics.GenericAPIView):

    serializer_class = CatalogoSerializer
    queryset = CatalogoArticulos.objects.all()

    # Get all articles
    def get(self, request):
        print(request)
        catalogo = CatalogoArticulos.objects.all()  # .get(ID=request.GET.get("id"))
        articulo = self.serializer_class(catalogo, many=True)
        return JsonResponse(articulo.data, safe=False)


class InsertProduct(generics.GenericAPIView):
    serializer_class = CatalogoSerializer
    queryset = CatalogoArticulos.objects.all()

    # Post an article if no exists
    def post(self, request):

        post_data = self.format_data(request)
        SKU = CatalogoArticulos.objects.filter(SKU=post_data["SKU"])

        if SKU.exists():

            return JsonResponse(
                {"status": "fail", "request": "El SKU ya existe"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            serializer = self.serializer_class(data=post_data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(
                    {"status": "success", "request": serializer.data},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return JsonResponse(
                    {"status": "fail", "request": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST,
                )

    # It creates logs per api endpoint
    def format_data(self, request):
        final = {
            "ID": request.data["id"],
            "SKU": request.data["title"],
            "ImagenURI": "None"
            if len(request.data["images"]) == 0
            else request.data["images"]["src"],
            "Nombre": request.data["title"],
            "Cantidad": request.data["variants"][0]["inventory_quantity"],
            "FechaRegistro": request.data["created_at"],
            "UltimaFechaActualizacion": request.data["updated_at"],
            "Sincronizado": True,
            "logs": [
                {
                    "Json": json.dumps(request.data),
                    "FechaRegistro": str(date.today()),
                }
            ],
        }
        return final


class UpdateProduct(generics.GenericAPIView):
    serializer_class = CatalogoSerializer
    queryset = CatalogoArticulos.objects.all()

    # Update an article stock if exists
    def post(self, request):
        update_data = self.format_data(request)
        catalogo_existente = CatalogoArticulos.objects.get(ID=update_data["ID"])
        serializer = self.serializer_class(catalogo_existente, data=update_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(
                {"status": "success", "request": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        else:
            return JsonResponse(
                {"status": "fail", "request": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    # It creates logs per api endpoint
    def format_data(self, request):
        final = {
            "ID": request.data["id"],
            "SKU": request.data["title"],
            "ImagenURI": "None"
            if len(request.data["images"]) == 0
            else request.data["images"]["src"],
            "Nombre": request.data["title"],
            "Cantidad": request.data["variants"][0]["inventory_quantity"],
            "FechaRegistro": request.data["created_at"],
            "UltimaFechaActualizacion": request.data["updated_at"],
            "Sincronizado": True,
            "logs": [
                {
                    "Json": json.dumps(request.data),
                    "FechaRegistro": str(date.today()),
                }
            ],
        }
        print(final)
        return final


class DeleteProduct(generics.GenericAPIView):
    serializer_class = CatalogoSerializer
    queryset = CatalogoArticulos.objects.all()

    def post(self, request):
        catalogo_existente = CatalogoArticulos.objects.get(ID=request.data["id"])
        catalogo_existente.delete()
        return JsonResponse("Deleted to Successfully", safe=False)


# Views for invoices


class SetInvoice(generics.GenericAPIView):
    serializer_class = FacturacionEncabezadoSerializer
    queryset = FacturacionEncabezado.objects.all()

    def post(self, request):

        post_data = self.format_data(request)
        ID = CatalogoArticulos.objects.filter(ID=post_data["ID"])

        if ID.exists():
            return JsonResponse(
                {"status": "fail", "request": "La Factura ya existe"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            serializer = self.serializer_class(data=post_data)

            if serializer.is_valid():
                serializer.save()
                return JsonResponse(
                    {"status": "success", "request": serializer.data},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return JsonResponse(
                    {"status": "fail", "request": serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST,
                )

    # It creates logs per api endpoint
    def format_data(self, request):
        invoice_id = request.data["id"]

        final = {
            "ID": invoice_id,
            "NumerOrden": request.data["order_number"],
            "Total": request.data["total_price"],
            "Moneda": request.data["currency"],
            "Fecha": request.data["created_at"],
            "cliente": [
                {
                    "Nombre": request.data["customer"]["first_name"]
                    + " "
                    + request.data["customer"]["last_name"],
                    "Telefono": request.data["customer"]["phone"]
                    if request.data["customer"]["phone"]
                    else "None",
                    "Correo": request.data["customer"]["email"],
                    "Direccion": request.data["customer"]["default_address"][
                        "address1"
                    ],
                }
            ],
            "detalle": [],
        }

        # print(request.data["line_items"])

        for product in request.data["line_items"]:
            final["detalle"].append(
                {
                    "ID": product["id"],
                    "SKU": product["sku"],
                    "ImagenURL": "None",
                    "Nombre": product["title"],
                    "Cantidad": product["quantity"],
                    "Precio": product["price"],
                    "Total": product["quantity"] * product["price"],
                }
            )
        return final


class GetInvoice(generics.GenericAPIView):
    serializer_class = FacturacionEncabezadoSerializer
    queryset = FacturacionEncabezado.objects.all()

    def get(self, request):
        invoices = FacturacionEncabezado.objects.all()  # .get(ID=request.GET.get("id"))
        serialized_invoices = self.serializer_class(invoices, many=True)
        return JsonResponse(serialized_invoices.data, safe=False)


class GetInvoiceID(generics.GenericAPIView):
    serializer_class = FacturacionEncabezadoSerializer
    queryset = FacturacionEncabezado.objects.all()

    def get(self, request, id, *args, **kwargs):
        invoice_id = id
        invoices = FacturacionEncabezado.objects.get(ID=invoice_id)
        serialized_invoices = self.serializer_class(invoices, many=True)
        return JsonResponse(serialized_invoices.data, safe=False)