# Generated by Django 3.0.6 on 2020-07-27 08:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_auto_20200727_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 6, 8, 13, 21, 98968, tzinfo=utc)),
        ),
    ]
