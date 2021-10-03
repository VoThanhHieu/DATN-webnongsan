from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.home, name="home"),
    path('index', views.Index, name="index"),
    # path('shop', views.Shop, name="shop"),
    # path('shop/<int:detail_id>', views.Shop, name="shop_product"),
    # path('login', views.Login, name="login"),
    path('checkout',views.Checkout,name="checkout"),
    path('contact',views.Contact, name="contact"),
    path('blog',views.Blog, name="blog"),
    path('about',views.About, name="about"),
    path('help',views.Help, name="help"),
    path('dathang',views.Dathang, name="dathang"),
    path('helphuy',views.Helphuy, name="helphuy"),
    path('order_profile',views.Order_profile, name="order_profile"),
    path('address',views.Address, name="address"),
    path('update_address',views.Update_address, name="update_address"),
    path('blog-single/<int:id>',views.Blogsingle, name="blogsingle"),
    path('product-single/<int:product_id>',views.Productsingle, name='product'),
    path('product-single/addcomment/<int:id>',views.addcomment, name="addcomment"),
    path('information',views.Information, name="information"),
    # path('blog-single/<int:id>',views.Blogsingle, name='blogcontent'),
    # path('cart',views.Cart, name="cart"),
    # path('register',views.Register, name="register")
]
