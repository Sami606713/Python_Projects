# Generated by Django 4.1.13 on 2024-01-05 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0063_order_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
    ]
