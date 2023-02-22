# Generated by Django 4.1.7 on 2023-03-27 13:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0022_payment_moneybird_financial_statement_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="moneybird_financial_mutation_id",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="moneybird financial mutation id",
            ),
        ),
    ]