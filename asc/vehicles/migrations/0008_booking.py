# Generated by Django 4.0.2 on 2022-03-23 15:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0007_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('vname', models.CharField(max_length=50)),
                ('address', models.CharField(default='', max_length=500)),
                ('phone', models.IntegerField(default=0)),
                ('cnic', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default=0)),
                ('branch', models.CharField(default='', max_length=500)),
                ('booking_time', models.DateTimeField(default=datetime.datetime(2022, 3, 23, 20, 4, 17, 121730), null=True)),
            ],
        ),
    ]
