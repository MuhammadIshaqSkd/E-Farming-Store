# Generated by Django 4.0.2 on 2022-03-23 15:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_alter_complete_deliverd_time_alter_order_order_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complete',
            name='deliverd_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 23, 20, 9, 30, 467759), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 23, 20, 9, 30, 467759), null=True),
        ),
    ]
