# Generated by Django 2.1.4 on 2018-12-17 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0027_auto_20181024_2000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ('first_name', 'last_name'), 'permissions': (('sentry_access', 'Access the Sentry backend'), ('nextcloud_admin', 'Access NextCloud as admin'))},
        ),
    ]