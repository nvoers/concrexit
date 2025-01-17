# Generated by Django 4.0.4 on 2022-05-27 07:44
from django.db import migrations, models
import thaliawebsite.storage.backend

class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0023_delete_partnerevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='logo',
            field=models.ImageField(storage=thaliawebsite.storage.backend.get_public_storage, upload_to='partners/logos/'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='site_header',
            field=models.ImageField(blank=True, null=True, storage=thaliawebsite.storage.backend.get_public_storage, upload_to='partners/headers/'),
        ),
        migrations.AlterField(
            model_name='partnerimage',
            name='image',
            field=models.ImageField(storage=thaliawebsite.storage.backend.get_public_storage, upload_to='partners/images/'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='company_logo',
            field=models.ImageField(blank=True, null=True, storage=thaliawebsite.storage.backend.get_public_storage, upload_to='partners/vacancy-logos/', verbose_name='company logo'),
        ),
    ]
