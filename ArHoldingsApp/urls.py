from django.urls import path, include
from rest_framework import routers
from ArHoldingsApp.views import (
    CustomAuthToken,
    InsertProduct,
    UpdateProduct,
    DeleteProduct,
    GetProducts,
    SetInvoice,
    GetInvoice,
)

# roter = routers.DefaultRouter()
# roter.register(r"products/getProducts", GetProducts, basename="get_products")
# roter.register(r"products/insertProduct", InsertProduct)
# roter.register(r"products/updateProduct", UpdateProduct)
# roter.register(r"products/deleteProduct", DeleteProduct)
# roter.register(r"invoice/setInvoice", SetInvoice)
# roter.register(r"invoice/getInvoice", GetInvoice)
# roter.register(r"invoice/getInvoice/(?P<id>\d+)", GetInvoice)


urlpatterns = [
    # # Catalogo
    path(r"products/insertProduct/", InsertProduct.as_view()),
    path(r"products/updateProduct/", UpdateProduct.as_view()),
    path(r"products/deleteProduct/", DeleteProduct.as_view()),
    path(r"products/getProducts/", GetProducts.as_view()),
    path(r"invoice/setInvoice/", SetInvoice.as_view()),
    path(r"invoice/getInvoice/", GetInvoice.as_view()),
    path(r"invoice/getInvoice/<int:pk>", GetInvoice.as_view()),
    path("token/auth/", CustomAuthToken.as_view()),
]

# 1197085556960 Insert product
# 1197085589728 Delete product
# 1197080576224 Insert invoice
