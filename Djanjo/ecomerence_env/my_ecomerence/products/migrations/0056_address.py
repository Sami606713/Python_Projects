# Generated by Django 4.1.13 on 2024-01-04 18:59

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0055_delete_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('mobile', models.CharField(help_text='+12345678', max_length=20)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('province', models.CharField(choices=[('Azad Kashmir', 'Azad Kashmir'), ('Balochistan', 'Balochistan'), ('Islamabad', 'Islamabad'), ('KPK', 'KPK'), ('Punjab', 'Punjab'), ('Sindh', 'Sindh')], max_length=50)),
                ('city', models.CharField(choices=[('haripur', 'haripur'), ('Abbottabad', 'Abbottabad'), ('Mansehera', 'Mansehra'), ('Hattar', 'Hattar'), ('Ghazi', 'Ghazi')], max_length=50)),
                ('area', models.CharField(choices=[('Pharhala', 'Pharhala'), ('K.T.S', 'K.T.S'), ('Amir khan plaza', 'Amir Khan Plaza')], max_length=50)),
            ],
        ),
    ]
