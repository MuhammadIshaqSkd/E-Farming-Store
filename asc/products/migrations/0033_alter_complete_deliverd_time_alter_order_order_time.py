# Generated by Django 4.0.4 on 2022-06-29 17:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_complete_city_alter_complete_deliverd_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complete',
            name='deliverd_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 29, 22, 36, 43, 535388), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 29, 22, 36, 43, 533387), null=True),
        ),
    ]
