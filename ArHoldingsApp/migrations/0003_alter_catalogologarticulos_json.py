# Generated by Django 4.1.7 on 2023-03-07 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArHoldingsApp', '0002_alter_catalogoarticulos_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogologarticulos',
            name='Json',
            field=models.CharField(max_length=10000),
        ),
    ]
