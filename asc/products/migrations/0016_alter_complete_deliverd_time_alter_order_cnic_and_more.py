# Generated by Django 4.0.2 on 2022-03-17 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_deliver_profile_pic_alter_complete_deliverd_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complete',
            name='deliverd_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 17, 21, 37, 47, 208333), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='cnic',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 17, 21, 37, 47, 208333), null=True),
        ),
    ]
