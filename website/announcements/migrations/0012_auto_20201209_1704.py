# Generated by Django 3.1.4 on 2020-12-09 16:04

import announcements.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0011_remove_multilang_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='content',
            field=models.FileField(help_text='The content of the slide; what image to display.', upload_to='public/announcements/slides/', validators=[announcements.models.validate_image], verbose_name='Content'),
        ),
    ]