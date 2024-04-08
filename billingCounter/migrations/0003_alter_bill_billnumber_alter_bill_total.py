# Generated by Django 5.0.4 on 2024-04-07 15:51

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billingCounter', '0002_alter_product_price_bill_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='billNumber',
            field=models.CharField(default=uuid.UUID('e4d0be6a-b48b-46d9-af26-f4336edf85bb'), max_length=200),
        ),
        migrations.AlterField(
            model_name='bill',
            name='total',
            field=models.FloatField(default=0.0),
        ),
    ]
