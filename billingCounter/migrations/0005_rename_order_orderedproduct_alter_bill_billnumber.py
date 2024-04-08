# Generated by Django 5.0.4 on 2024-04-08 16:14

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billingCounter', '0004_product_quantity_alter_bill_billnumber'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='OrderedProduct',
        ),
        migrations.AlterField(
            model_name='bill',
            name='billNumber',
            field=models.CharField(default=uuid.UUID('cc880aef-929a-4403-9830-1840c9c51ed8'), max_length=200),
        ),
    ]