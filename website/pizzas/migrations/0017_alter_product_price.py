# Generated by Django 3.2.10 on 2021-12-16 22:00

from django.db import migrations
import payments.models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0016_alter_foodorder_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=payments.models.PaymentAmountField(decimal_places=2, max_digits=8, validators=[payments.models.validate_not_zero]),
        ),
    ]
