# Generated by Django 3.1.6 on 2021-09-16 07:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='complete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliverd_time', models.DateTimeField(default=datetime.datetime(2021, 9, 16, 0, 1, 39, 491628), null=True)),
                ('deliver_cnic', models.IntegerField(default=0)),
                ('order_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 16, 0, 1, 39, 491628), null=True),
        ),
    ]
