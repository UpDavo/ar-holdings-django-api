from django.urls import re_path
from ArHoldingsApp.views import (
    InsertProduct,
    UpdateProduct,
    DeleteProduct,
    GetProducts,
    SetInvoice,
    GetInvoice,
    GetInvoiceID,
)


urlpatterns = [
    # Catalogo
    re_path(r"products/insertProduct", InsertProduct.as_view()),
    re_path(r"products/updateProduct", UpdateProduct.as_view()),
    re_path(r"products/deleteProduct", DeleteProduct.as_view()),
    re_path(r"products/getProducts", GetProducts.as_view()),
    re_path(r"invoice/setInvoice", SetInvoice.as_view()),
    re_path(r"invoice/getInvoice", GetInvoice.as_view()),
    re_path(r"^invoice/getInvoice/(?P<id>\d+)/$", GetInvoiceID.as_view()),
    # Logs de Catalogo
]

# 1197085556960 Insert
# 1197085589728 Delete
# 1197085655264 Update
