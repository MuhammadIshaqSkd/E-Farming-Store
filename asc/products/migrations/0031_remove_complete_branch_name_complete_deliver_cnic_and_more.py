# Generated by Django 4.0.2 on 2022-04-15 16:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_remove_complete_deliver_cnic_complete_branch_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complete',
            name='branch_name',
        ),
        migrations.AddField(
            model_name='complete',
            name='deliver_cnic',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='complete',
            name='deliverd_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 15, 21, 0, 59, 535777), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 15, 21, 0, 59, 520152), null=True),
        ),
    ]
