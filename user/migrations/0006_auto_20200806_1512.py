# Generated by Django 3.0.6 on 2020-08-06 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_auto_20200802_1437'),
        ('user', '0005_auto_20200802_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.ForeignKey(blank=True, default=14, on_delete=django.db.models.deletion.CASCADE, to='home.City'),
        ),
    ]
