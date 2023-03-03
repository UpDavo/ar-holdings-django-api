# Generated by Django 4.1.7 on 2023-03-03 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogoArticulos',
            fields=[
                ('ID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('SKU', models.CharField(max_length=20)),
                ('ImagenURI', models.CharField(max_length=1000)),
                ('Nombre', models.CharField(max_length=1000)),
                ('Cantidad', models.IntegerField()),
                ('FechaRegistro', models.CharField(max_length=1000)),
                ('UltimaFechaActualizacion', models.CharField(max_length=1000)),
                ('Sincronizado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='FacturacionEncabezado',
            fields=[
                ('ID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('NumerOrden', models.CharField(max_length=20)),
                ('Total', models.IntegerField()),
                ('Moneda', models.CharField(max_length=1000)),
                ('Fecha', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='FacturacionDetalle',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('SKU', models.CharField(max_length=40)),
                ('ImagenURL', models.CharField(max_length=3000)),
                ('Nombre', models.CharField(max_length=1000)),
                ('Cantidad', models.IntegerField()),
                ('Precio', models.IntegerField()),
                ('Total', models.IntegerField()),
                ('IdEncabezado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArHoldingsApp.facturacionencabezado')),
            ],
        ),
        migrations.CreateModel(
            name='FacturacionCliente',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=1000)),
                ('Telefono', models.CharField(max_length=1000)),
                ('Correo', models.CharField(max_length=1000)),
                ('Direccion', models.CharField(max_length=1000)),
                ('IdEncabezado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ArHoldingsApp.facturacionencabezado')),
            ],
        ),
        migrations.CreateModel(
            name='CatalogoLogArticulos',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Json', models.CharField(max_length=3000)),
                ('FechaRegistro', models.CharField(max_length=1000)),
                ('IdArticulo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='ArHoldingsApp.catalogoarticulos')),
            ],
        ),
    ]
