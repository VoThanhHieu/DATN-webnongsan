from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
# from django.core.signals import line_cost
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput
from home.models import City, district, ward
# Create your models here.

from home.models import Product

class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name
    
    @property
    def price(self):
        return (self.product.price)

    @property
    def amount(self):
        return (self.quantity * self.product.price)

class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']
        widgets = {
            'quantity' : TextInput(attrs={'class':'input', 'type':'number','value':'1'}),
        }

class Entry(models.Model):
        product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
        sCart = models.ForeignKey(ShopCart, on_delete=models.SET_NULL, null=True)
        quantity = models.PositiveIntegerField()

# @receiver(post_save, sender=Entry)
# def update_cart(sender, instance, **kwargs):
#     line_cost = instance.quantity * instance.product.price
#     instance.cart.count = int(instance.cart.count) + int(instance.quantity)

class Shipper(models.Model):
    shipper_name = models.CharField(max_length=200)
    def __str__(self):
        return str(self.shipper_name)

class Order(models.Model):
    STATUS= (
        ('Mới', 'Mới'),
        ('Đã Xác Nhận', 'Đã Xác Nhận'),
        ('Đang Vận Chuyển', 'Đang Vận Chuyển'),
        ('Hoàn Thành', 'Hoàn Thành'),
        ('Đã Hủy', 'Đã Hủy'),
        ('Đang Đóng Gói', 'Đang Đóng Gói'),
    )
    user = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    shipper = models.ForeignKey(Shipper, on_delete= models.SET_NULL, blank=True, null=True)
    code = models.CharField(max_length=5, editable=False)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    country = models.ForeignKey(district,on_delete=models.SET_NULL, blank=True, null=True)
    ward = models.ForeignKey(ward,on_delete=models.SET_NULL, blank=True, null=True)
    total = models.FloatField()
    status = models.CharField(max_length=20, choices=STATUS, default='Mới')
    ip = models.CharField(blank=True, max_length=20)
    adminnote = models.CharField(blank=True, max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=10))

    def __str__(self):
        # return self.user.first_name
        return str(self.user.first_name)
        

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name','last_name','address','phone','city','country', 'ward']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country'].queryset = district.objects.none()
        if 'city' in self.data:
            try:
                country_id = int(self.data.get('city'))
                self.fields['country'].queryset = district.objects.filter(city_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk:
            self.fields['country'].queryset = self.instance.city.country_set.order_by('name')
        
        self.fields['ward'].queryset = ward.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['ward'].queryset = ward.objects.filter(district_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk:
            self.fields['ward'].queryset = self.instance.country.ward.order_by('name')

class OrderProduct(models.Model):
    STATUS= (
        ('Mới', 'Mới'),
        ('Cũ', 'Cũ'),
        ('Hết Han', 'Hết Han'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    amount = models.FloatField()
    status = models.CharField(max_length=20, choices=STATUS, default='Mới')
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return self.product.title
        return str(self.product.name)
        
        
