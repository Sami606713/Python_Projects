# Generated by Django 4.1.13 on 2024-01-06 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0067_remove_products_image_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(default='', upload_to='media/images'),
        ),
    ]
