# Generated by Django 4.1.13 on 2023-12-16 21:35

from django.db import migrations
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_alter_products_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='item_id',
            field=djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]