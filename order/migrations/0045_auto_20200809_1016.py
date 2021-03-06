# Generated by Django 3.0.6 on 2020-08-09 03:16

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0044_auto_20200806_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipper',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.Shipper'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Mới', 'Mới'), ('Đã Xác Nhận', 'Đã Xác Nhận'), ('Đang Vận Chuyển', 'Đang Vận Chuyển'), ('Hoàn Thành', 'Hoàn Thành'), ('Đã Hủy', 'Đã Hủy'), ('Đang Đóng Gói', 'Đang Đóng Gói')], default='Mới', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 3, 16, 2, 70856, tzinfo=utc)),
        ),
    ]
