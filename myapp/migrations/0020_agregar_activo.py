# Generated by Django 5.1.2 on 2024-10-25 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_remove_agregar_codigo_qr'),
    ]

    operations = [
        migrations.AddField(
            model_name='agregar',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
