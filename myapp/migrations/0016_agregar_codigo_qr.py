# Generated by Django 5.1.2 on 2024-10-24 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_elemento_notificacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='agregar',
            name='codigo_qr',
            field=models.ImageField(blank=True, null=True, upload_to='qr_codes'),
        ),
    ]