# Generated by Django 3.1.6 on 2021-07-28 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210727_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Delivery',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='order',
            name='branch',
            field=models.CharField(default='', max_length=200),
        ),
    ]
