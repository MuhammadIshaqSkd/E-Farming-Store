# Generated by Django 3.1.6 on 2021-07-28 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='list',
            new_name='branch',
        ),
    ]
