# Generated by Django 3.0.6 on 2020-05-26 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_product_product_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='chitiet',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]