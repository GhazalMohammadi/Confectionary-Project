# Generated by Django 4.2.2 on 2023-07-01 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_cart_product_unit'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
