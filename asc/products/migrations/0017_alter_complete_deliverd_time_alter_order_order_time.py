# Generated by Django 4.0.2 on 2022-03-19 11:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_complete_deliverd_time_alter_order_cnic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complete',
            name='deliverd_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 19, 16, 47, 56, 140576), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 19, 16, 47, 56, 140576), null=True),
        ),
    ]
