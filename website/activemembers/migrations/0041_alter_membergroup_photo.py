# Generated by Django 4.0.4 on 2022-05-27 07:44
import os

from django.db import migrations, models

import thaliawebsite.storage.backend


def forwards_func(apps, schema_editor):
    MemberGroup = apps.get_model('activemembers', 'MemberGroup')

    existing_images = []

    for item in MemberGroup.objects.filter(photo__isnull=False):
        item.photo.name = item.photo.name[7:]
        existing_images.append(item.photo.name)
        item.save()

    # This deletes unused images from the filesystem
    storage = MemberGroup().photo.storage
    if storage.exists("committeephotos"):
        files = set(storage.listdir("committeephotos")[1])
        existing_images = set(map(lambda x: os.path.basename(x), existing_images))
        for file in files.difference(existing_images):
            storage.delete(f"committeephotos/{file}")


def reverse_func(apps, schema_editor):
    MemberGroup = apps.get_model('activemembers', 'MemberGroup')

    for item in MemberGroup.objects.filter(photo__isnull=False):
        item.photo.name = f"public/{item.photo.name}"
        item.save()

class Migration(migrations.Migration):

    dependencies = [
        ('activemembers', '0040_remove_multilang_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membergroup',
            name='photo',
            field=models.ImageField(blank=True, null=True, storage=thaliawebsite.storage.backend.get_public_storage, upload_to='committeephotos/', verbose_name='Image'),
        ),
        migrations.RunPython(forwards_func, reverse_func),
    ]
