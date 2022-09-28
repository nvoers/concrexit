# Generated by Django 4.0.7 on 2022-09-07 09:03

import uuid

from django.db import migrations


def gen_mark_present_url_token(apps, schema_editor):
    Event = apps.get_model("events", "Event")
    for row in Event.objects.all():
        row.mark_present_url_token = uuid.uuid4()
        row.save(update_fields=["mark_present_url_token"])


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0056_event_mark_present_url_token"),
    ]

    operations = [
        migrations.RunPython(
            gen_mark_present_url_token,
            reverse_code=migrations.RunPython.noop,
        ),
    ]