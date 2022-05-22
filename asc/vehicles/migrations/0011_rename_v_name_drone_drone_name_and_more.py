# Generated by Django 4.0.2 on 2022-03-23 16:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0010_rename_v_name_tool_tool_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drone',
            old_name='v_name',
            new_name='drone_name',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='v_name',
            new_name='vehicle_name',
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 23, 21, 7, 49, 489380), null=True),
        ),
    ]
