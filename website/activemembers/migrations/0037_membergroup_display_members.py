# Generated by Django 2.1.5 on 2019-02-06 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activemembers', '0036_auto_20181024_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='membergroup',
            name='display_members',
            field=models.BooleanField(default=False),
        ),
    ]
