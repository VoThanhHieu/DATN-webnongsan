# Generated by Django 3.0.6 on 2020-07-07 14:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_auto_20200530_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_use',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
