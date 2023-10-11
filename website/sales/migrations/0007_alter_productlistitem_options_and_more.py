# Generated by Django 4.2.5 on 2023-10-04 18:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sales", "0006_order_is_free_order_total_amount"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="productlistitem",
            options={
                "ordering": ("-priority",),
                "verbose_name": "product",
                "verbose_name_plural": "products",
            },
        ),
        migrations.AddField(
            model_name="productlistitem",
            name="priority",
            field=models.IntegerField(
                default=1,
                verbose_name="priority",
                help_text="Determines the order of the products in the list, highest first.",
            ),
        ),
    ]