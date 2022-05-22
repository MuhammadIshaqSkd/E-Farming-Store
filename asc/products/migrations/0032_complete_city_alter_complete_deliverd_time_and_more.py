# Generated by Django 4.0.2 on 2022-04-15 16:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_remove_complete_branch_name_complete_deliver_cnic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='complete',
            name='city',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='complete',
            name='deliverd_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 15, 21, 6, 50, 257960), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 15, 21, 6, 50, 257960), null=True),
        ),
    ]
