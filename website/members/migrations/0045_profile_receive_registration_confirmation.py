# Generated by Django 4.1.7 on 2023-03-17 15:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("members", "0044_alter_profile_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="receive_registration_confirmation",
            field=models.BooleanField(
                default=True,
                help_text="Receive confirmation emails when registering for events",
                verbose_name="Receive registration confirmations",
            ),
        ),
    ]