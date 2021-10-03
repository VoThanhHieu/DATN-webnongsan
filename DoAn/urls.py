"""DoAn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from home import views 
from django.conf.urls import url
from django_filters.views import FilterView
from order import views as OrderViews
from user import views as UserViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/',include('accounts.urls')),
    path('order/',include('order.urls')),
    path('user/',include('user.urls')),
    path('shop/', views.Shop, name="shop"),
    path('shop/<int:detail_id>/', views.shop_product, name="shop_product"),
    path('shopcart',OrderViews.shopcart, name="shopcart"),
    path('login/', UserViews.login_form, name="login_form"),
    path('logout/', UserViews.logout_form, name="logout_form"),
    path('signup/', UserViews.singup_form, name="singup_form"),
    path('s/', views.Search, name="search"),
    url(r'^report/$', views.searchreport, name='searchreport'),
    url(r'^reportproduct/$', views.searchreportproduct, name='searchreportproduct'),
    path('report/',views.Report, name="report"),
    path('reportproduct/',views.Reportproduct, name="reportproduct"),
    path('addcomment/<int:id>',views.addcomment, name="addcomment"),

    
    # path('shopcart/<int:id>/(?P<qty>\d+)',OrderViews.shopcart, name="update_cart"),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)