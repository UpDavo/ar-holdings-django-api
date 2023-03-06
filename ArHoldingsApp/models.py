from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# Artículos del catálogo


class CatalogoArticulos(models.Model):
    ID = models.CharField(max_length=20, primary_key=True)
    SKU = models.CharField(max_length=20)
    ImagenURI = models.CharField(max_length=1000)
    Nombre = models.CharField(max_length=1000)
    Cantidad = models.IntegerField()
    FechaRegistro = models.CharField(max_length=1000)
    UltimaFechaActualizacion = models.CharField(max_length=1000)
    Sincronizado = models.BooleanField()

    def __str__(self):
        return str(self.ID)


class CatalogoLogArticulos(models.Model):
    ID = models.AutoField(primary_key=True)
    IdArticulo = models.ForeignKey(
        CatalogoArticulos,
        on_delete=models.CASCADE,
        related_name="logs",
        null=True,
        blank=True,
    )
    Json = models.CharField(max_length=3000)
    FechaRegistro = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.IdArticulo)

    @property
    def logs(self):
        return self.logs_set.all()


# Facturación


class FacturacionEncabezado(models.Model):
    ID = models.CharField(max_length=20, primary_key=True)
    NumerOrden = models.CharField(max_length=20)
    Total = models.IntegerField()
    Moneda = models.CharField(max_length=1000)
    Fecha = models.CharField(max_length=1000)

    def __str__(self):
        return self.NumerOrden

    @property
    def cliente(self):
        return self.cliente_set.all()

    @property
    def detalle(self):
        return self.detalle_set.all()


class FacturacionDetalle(models.Model):
    ID = models.CharField(max_length=20, primary_key=True)
    SKU = models.CharField(max_length=20)
    IdEncabezado = models.ForeignKey(
        FacturacionEncabezado,
        on_delete=models.CASCADE,
        related_name="detalle",
        null=True,
        blank=True,
    )
    ImagenURL = models.CharField(max_length=3000)
    Nombre = models.CharField(max_length=1000)
    Cantidad = models.IntegerField()
    Precio = models.IntegerField()
    Total = models.IntegerField()

    def __str__(self):
        return self.Nombre


class FacturacionCliente(models.Model):
    ID = models.AutoField(primary_key=True)
    IdEncabezado = models.ForeignKey(
        FacturacionEncabezado,
        on_delete=models.CASCADE,
        related_name="cliente",
        null=True,
        blank=True,
    )
    Nombre = models.CharField(max_length=1000)
    Telefono = models.CharField(max_length=1000)
    Correo = models.CharField(max_length=1000)
    Direccion = models.CharField(max_length=1000)

    def __str__(self):
        return self.Nombre
