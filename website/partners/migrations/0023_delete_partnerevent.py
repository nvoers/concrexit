# Generated by Django 3.2.8 on 2021-10-30 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0022_move_to_external_events'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PartnerEvent',
        ),
    ]