# Generated by Django 4.1.13 on 2023-12-08 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_products_date_alter_products_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('Electronic', 'Electronic'), ('Fashion', 'Fashion'), ('Education', 'Education'), ('Vehicle', 'Vehicles')], max_length=20),
        ),
    ]
