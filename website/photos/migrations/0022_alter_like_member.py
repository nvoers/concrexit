# Generated by Django 4.2 on 2023-04-13 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0044_alter_profile_photo"),
        ("photos", "0021_alter_photo_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="like",
            name="member",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="members.member",
            ),
        ),
    ]