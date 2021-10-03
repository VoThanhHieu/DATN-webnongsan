from django import forms
from order.models import Order
import django_filters
from django_filters.widgets import DateRangeWidget
from home.models import Product, Product_detail

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = ('name',)

class ExportFilter(django_filters.FilterSet):
    create_date = django_filters.DateFilter(field_name='create_date', label='Chọn Tháng Ban Muốn Thống Kê'),
    create_date_gte = django_filters.DateFilter(field_name='create_date',name='update_date_gte', lookup_type='gte', label='Date minimale'),
    create_date_lte = django_filters.DateFilter(field_name='create_date',name='update_date_lte', lookup_type='lte', label='Date maximale'),
    status = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Order
        fields = {
            'create_date': ['gte', 'lte'],
            'status':[],
        }

class ExportProductFilter(django_filters.FilterSet):
    quantities = django_filters.NumberFilter(field_name='quantities',lookup_type='lte', label='Số Lượng Tồn'),
    quantities_lte = django_filters.NumberFilter(field_name='quantities',name='quantities_lte' ,lookup_type='lte', label='Số Lượng Tồn'),
    name = django_filters.CharFilter(lookup_expr='icontains')
    date_use = django_filters.DateFilter(field_name='date_use', label='Chọn Tháng Ban Muốn Thống Kê'),
    date_use_lte = django_filters.DateFilter(field_name='date_use',name='date_use_lte', lookup_type='lte', label='Date maximale'),
    class Meta:
        model = Product
        fields = {
            'quantities': ['lte'],
            'name':[],
            'date_use':['lte']
        }
