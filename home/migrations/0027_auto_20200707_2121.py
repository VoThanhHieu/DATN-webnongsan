# Generated by Django 3.0.6 on 2020-07-07 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0026_product_date_use'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=100),
        ),
    ]
