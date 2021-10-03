# Generated by Django 3.0.6 on 2020-08-09 04:28

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0048_auto_20200809_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipper',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.Shipper'),
        ),
        migrations.AlterField(
            model_name='order',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 4, 28, 35, 713214, tzinfo=utc)),
        ),
    ]
