# Generated by Django 4.0.2 on 2022-03-27 08:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0012_branche_alter_booking_booking_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('complaint_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.IntegerField(default=0)),
                ('complaint_type', models.CharField(default='', max_length=20)),
                ('complaint_details', models.CharField(default='', max_length=1000)),
                ('complaint_time', models.DateTimeField(default=datetime.datetime(2022, 3, 27, 13, 17, 21, 117882), null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 27, 13, 17, 21, 102279), null=True),
        ),
        migrations.AlterField(
            model_name='branche',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 27, 13, 17, 21, 102279), null=True),
        ),
    ]
