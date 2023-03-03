from rest_framework import serializers
from ArHoldingsApp.models import (
    CatalogoArticulos,
    CatalogoLogArticulos,
    FacturacionEncabezado,
    FacturacionCliente,
    FacturacionDetalle,
)


# Catalogo


class CatalogoLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogoLogArticulos
        fields = "__all__"

    read_only_fields = ("IdArticulo",)


class CatalogoSerializer(serializers.ModelSerializer):

    logs = CatalogoLogSerializer(many=True)

    class Meta:
        model = CatalogoArticulos
        fields = "__all__"

    def create(self, validated_data):
        logs_data = validated_data.pop("logs")
        articulo = CatalogoArticulos.objects.create(**validated_data)
        for log_data in logs_data:
            CatalogoLogArticulos.objects.create(IdArticulo=articulo, **log_data)
        return articulo

    def update(self, instance, validated_data):
        logs_data = validated_data.pop("logs")
        articulo = super().update(instance, validated_data)
        keep_logs = []
        for log_data in logs_data:
            if "ID" in log_data.keys():
                if CatalogoLogArticulos.objects.filter(ID=log_data["ID"]).exists():
                    log = CatalogoLogArticulos.objects.get(ID=log_data["ID"])
                    log.ID = log_data.get("ID", log.ID)
                    log.save()
                    keep_logs.append(log)
                else:
                    continue
            else:
                log = CatalogoLogArticulos.objects.create(
                    IdArticulo=instance, **log_data
                )
                keep_logs.append(log.ID)

        return articulo


# Facturación


class FacturacionDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacturacionDetalle
        fields = "__all__"
        read_only_fields = ("IdEncabezado",)


class FacturacionClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacturacionCliente
        fields = "__all__"
        read_only_fields = ("IdEncabezado",)


class FacturacionEncabezadoSerializer(serializers.ModelSerializer):

    cliente = FacturacionClienteSerializer(many=True)
    detalle = FacturacionDetalleSerializer(many=True)

    class Meta:
        model = FacturacionEncabezado
        fields = "__all__"

    def create(self, validated_data):
        cliente_data = validated_data.pop("cliente")
        detalle_data = validated_data.pop("detalle")
        encabezado = FacturacionEncabezado.objects.create(**validated_data)
        for cliente in cliente_data:
            FacturacionCliente.objects.create(IdEncabezado=encabezado, **cliente)
        for detalle in detalle_data:
            FacturacionDetalle.objects.create(IdEncabezado=encabezado, **detalle)
        return encabezado
