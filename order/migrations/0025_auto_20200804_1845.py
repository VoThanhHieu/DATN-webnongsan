# Generated by Django 3.0.6 on 2020-08-04 11:45

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0024_auto_20200802_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipper_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 14, 11, 45, 24, 266827, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='order',
            name='shipper',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.Shipper'),
        ),
    ]
