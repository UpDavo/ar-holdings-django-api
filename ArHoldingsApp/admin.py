from django.contrib import admin

from ArHoldingsApp.models import (
    CatalogoArticulos,
    CatalogoLogArticulos,
    FacturacionEncabezado,
    FacturacionDetalle,
    FacturacionCliente,
    # create_auth_token,
)

# Register your models here.

admin.site.register(CatalogoArticulos)
admin.site.register(CatalogoLogArticulos)
admin.site.register(FacturacionEncabezado)
admin.site.register(FacturacionDetalle)
admin.site.register(FacturacionCliente)
# admin.site.register(create_auth_token)
