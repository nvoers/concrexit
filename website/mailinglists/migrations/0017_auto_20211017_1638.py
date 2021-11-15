# Generated by Django 3.2.8 on 2021-10-17 14:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailinglists', '0016_auto_20191030_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailinglist',
            name='active_gsuite_name',
            field=models.CharField(blank=True, max_length=60, null=True, unique=True, validators=[django.core.validators.RegexValidator(message='Enter a simpler name', regex='^[a-zA-Z0-9-]+$'), django.core.validators.RegexValidator(message='The entered name is a reserved value', regex='^(?!(abuse|admin|administrator|hostmaster|majordomo|postmaster|root|ssl-admin|webmaster)$)')], verbose_name='Active GSuite name'),
        ),
        migrations.AlterField(
            model_name='mailinglist',
            name='name',
            field=models.CharField(help_text='Enter the name for the list (i.e. name@thalia.nu).', max_length=60, unique=True, validators=[django.core.validators.RegexValidator(message='Enter a simpler name', regex='^[a-zA-Z0-9-]+$'), django.core.validators.RegexValidator(message='The entered name is a reserved value', regex='^(?!(abuse|admin|administrator|hostmaster|majordomo|postmaster|root|ssl-admin|webmaster)$)')], verbose_name='Name'),
        ),
    ]