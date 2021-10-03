# Generated by Django 3.0.6 on 2020-08-09 04:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0046_auto_20200809_1021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shipper',
        ),
        migrations.AlterField(
            model_name='order',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 4, 26, 56, 443999, tzinfo=utc)),
        ),
    ]