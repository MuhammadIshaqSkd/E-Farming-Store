# Generated by Django 3.1.6 on 2021-09-16 10:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20210916_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='qty',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='complete',
            name='deliverd_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 3, 16, 35, 640429), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 3, 16, 35, 640429), null=True),
        ),
    ]
