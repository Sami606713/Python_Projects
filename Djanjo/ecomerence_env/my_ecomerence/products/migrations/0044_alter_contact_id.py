# Generated by Django 4.1.13 on 2023-12-19 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0043_alter_contact_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
