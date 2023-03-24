# Generated by Django 4.1.7 on 2023-03-05 07:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0015_alter_auctionproduct_end_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionproduct',
            name='status',
        ),
        migrations.AlterField(
            model_name='auctionproduct',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 5, 12, 32, 40, 460132)),
        ),
        migrations.AlterField(
            model_name='auctionproduct',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 5, 12, 32, 40, 460132)),
        ),
    ]