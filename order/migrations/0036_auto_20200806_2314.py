# Generated by Django 3.0.6 on 2020-08-06 16:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0035_auto_20200806_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 16, 16, 14, 48, 26340, tzinfo=utc)),
        ),
    ]
