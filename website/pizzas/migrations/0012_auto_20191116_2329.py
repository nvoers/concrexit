# Generated by Django 2.2.6 on 2019-11-16 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0011_auto_20191129_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pizzas_order', to='payments.Payment', verbose_name='payment'),
        ),
    ]
