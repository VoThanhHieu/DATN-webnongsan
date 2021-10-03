
from django.db import models

from django.contrib.auth.models import User
from datetime import datetime , timedelta

# Create your models here.
from django.forms import ModelForm
from django.db.models import Avg, Count



class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Product_detail(models.Model):
	product_id = models.IntegerField()
	product_name = models.CharField(max_length=50)
	def __str__(self):
		return str(self.product_name)

class Product_NCC(models.Model):
	product_NCCName = models.CharField(max_length=50)
	def __str__(self):
		return str(self.product_NCCName)

class Product_detail(models.Model):
	product_id = models.IntegerField()
	product_name = models.CharField(max_length=50)
	def __str__(self):
		return str(self.product_name)


class Product(models.Model):
	product_ncc = models.ForeignKey(Product_NCC, on_delete= models.SET_NULL, null=True, blank=True)
	product_detail = models.ForeignKey(Product_detail, on_delete=models.SET_NULL, null=True, blank=True)
	name = models.CharField(max_length=200)
	price = models.DecimalField(default = 1,max_digits=100,decimal_places=0)
	digital = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(null=True, blank=True)
	description = models.TextField()
	quantities = models.IntegerField()
	date_use = models.DateTimeField(auto_now_add=False,blank=True)
	pack = models.CharField(max_length=100, null=True)
	def __str__(self):
		return str(self.name)

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

	def avaregereview(self):
			reviews = Comment.objects.filter(product=self, status='True').aggregate(avarage=Avg('rate'))
			avg=0
			if reviews["avarage"] is not None:
				avg=float(reviews["avarage"])
			return avg

	def countreview(self):
			reviews = Comment.objects.filter(product=self, status='True').aggregate(count=Count('id'))
			cnt=0
			if reviews["count"] is not None:
				cnt = int(reviews["count"])
			return cnt

class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	ngaythem = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address

class Blogcontent_Single(models.Model):
	blog_id = models.IntegerField()
	title_name = models.CharField(max_length=300)
	
	def __str__(self):
		return str(self.title_name)

class Blogcontent(models.Model):
	blogcontent_Single = models.ForeignKey(Blogcontent_Single, on_delete=models.SET_NULL, null=True)
	title = models.CharField(max_length=300)
	slug = models.SlugField()
	body = models.TextField()
	body_text = models.TextField()
	body_content = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	image = models.ImageField(null=True, blank=True)
	image_text = models.ImageField(null=True, blank=True)
	
	def __str__(self):
		return (self.title)

	def snippet(self):
		return(self.body[:200] + '......')

# class SignUpForm(UserCreationForm):
#     username = forms.CharField(max_length=30,help_text='Tên đăng nhập', label='Tên đăng nhập: ')
#     email = forms.EmailField(max_length=100,help_text='Email',label='Email: ')
#     first_name = forms.CharField(max_length=100, help_text='Họ và đệm ',label='Họ và đệm:')
#     last_name = forms.CharField(max_length=100, help_text='Tên ', label='Tên:')

#     class Meta:
#         model = User
#         fields = ('username', 'email','first_name','last_name','password1','password2',)

class Comment(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.CharField(max_length=250,blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status=models.CharField(max_length=10,choices=STATUS, default='True')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class City(models.Model):
	name  = models.CharField(max_length=300)
	def __str__(self):
		return str(self.name)

class district(models.Model):
	city=models.ForeignKey(City,on_delete=models.CASCADE)
	name  = models.CharField(max_length=300)

	def __str__(self):
		return str(self.name)
class ward(models.Model):
	district=models.ForeignKey(district,on_delete=models.CASCADE)
	name  = models.CharField(max_length=300)
	def __str__(self):
		return str(self.name)
