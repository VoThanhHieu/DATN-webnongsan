# Generated by Django 3.0.6 on 2020-07-14 12:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_auto_20200711_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 24, 12, 31, 41, 723691, tzinfo=utc)),
        ),
    ]
