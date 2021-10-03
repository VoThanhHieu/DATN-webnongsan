from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index, name="home"),
    path('addtoshopcart/<int:id>', views.addtoshopcart, name="addtoshopcart"),
    path('deleteformcart/<int:id>', views.deleteformcart, name="deleteformcart"),
    path('ordertracking',views.OrderTracking, name="ordertracking"),
    path('orderproduct', views.orderproduct, name="orderproduct"),
    path('orderproductdetail/<int:id>', views.orderproductdetail, name="orderproductdetail"),
    path('deleteshop/<int:id>', views.deleteshop, name="deleteshop"),
    path('delete_single_item_from_cart/<int:id>', views.delete_single_item_from_cart, name = "delete_single_item_from_cart"),
    path('add_single_item_from_cart/<int:id>', views.add_single_item_from_cart, name = "add_single_item_from_cart"),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
    path('ajax/load-district/', views.load_district, name='ajax_load_district'),
    path('ordercancel',views.OrderCancel, name="ordercancel")


    # path('updatecart/<int:id>', views.updatecart, name="updatecart"),
]