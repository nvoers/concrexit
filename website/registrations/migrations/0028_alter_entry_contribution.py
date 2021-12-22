# Generated by Django 3.2.10 on 2021-12-16 22:00

import django.core.validators
from django.db import migrations
import payments.models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0027_alter_entry_membership'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='contribution',
            field=payments.models.PaymentAmountField(decimal_places=2, default=7.5, max_digits=8, validators=[django.core.validators.MinValueValidator(7.5), payments.models.validate_not_zero], verbose_name='contribution'),
        ),
    ]