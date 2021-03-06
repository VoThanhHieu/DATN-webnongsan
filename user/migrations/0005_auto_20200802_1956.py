# Generated by Django 3.0.6 on 2020-08-02 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0036_auto_20200802_1437'),
        ('user', '0004_userprofile_ward'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.ForeignKey(blank=True, default=45, on_delete=django.db.models.deletion.CASCADE, to='home.City'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=models.ForeignKey(blank=True, default=12, on_delete=django.db.models.deletion.CASCADE, to='home.district'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='ward',
            field=models.ForeignKey(blank=True, default=156, on_delete=django.db.models.deletion.CASCADE, to='home.ward'),
        ),
    ]
