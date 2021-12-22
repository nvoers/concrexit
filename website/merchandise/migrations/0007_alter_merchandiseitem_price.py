# Generated by Django 3.2.10 on 2021-12-16 21:57

from django.db import migrations
import payments.models


class Migration(migrations.Migration):

    dependencies = [
        ('merchandise', '0006_alter_merchandiseitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='merchandiseitem',
            name='price',
            field=payments.models.PaymentAmountField(decimal_places=2, max_digits=8, validators=[payments.models.validate_not_zero]),
        ),
    ]