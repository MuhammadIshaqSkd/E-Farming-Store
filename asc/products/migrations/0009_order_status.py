# Generated by Django 3.1.6 on 2021-09-14 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210914_0419'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='STATUS',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Recived', 'Recived')], default='Pending', max_length=50, null=True),
        ),
    ]
