from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from order.models import ShopCart, ShopCartForm, Order, OrderForm, OrderProduct
from home.models import City, district, ward
from django.utils.crypto import get_random_string
import json as simplejson    

# Create your views here.


from home.models import Product_detail, Product
from user.models import UserProfile

def index(request):
    return HttpResponse('Order page')
 

@login_required(login_url='/login')
def delete_single_item_from_cart(request,id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    checkproduct = ShopCart.objects.filter(product_id = id)
    data = ShopCart.objects.get(product_id=id)
    data.quantity -= 1
    data.save()
    messages.success(request, "Đã cập nhật giỏ hàng")
    return HttpResponseRedirect(url)

@login_required(login_url='/login')
def add_single_item_from_cart(request,id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    checkproduct = ShopCart.objects.filter(product_id = id)
    data = ShopCart.objects.get(product_id=id)
    data.quantity += 1
    data.save()
    messages.success(request, "Đã cập nhật giỏ hàng")
    return HttpResponseRedirect(url)


@login_required(login_url='/login')
def addtoshopcart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user

    checkproduct = ShopCart.objects.filter(product_id = id)    
    if checkproduct:
        control = 1
    else: 
        control = 0
    
    if request.method == 'POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control == 1:
                data = ShopCart.objects.get(product_id = id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
            else: 
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        messages.success(request, "Sản phẩm đã được thêm vào giỏ")
        return HttpResponseRedirect(url)

    else: 
        if control == 1:
            data = ShopCart.objects.get(product_id = id)
            data.quantity += 1
            data.save()
        else:
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()
        messages.success(request, "Sản phẩm đã được thêm vào giỏ")
        return HttpResponseRedirect(url)

def shopcart(request):
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:10]
    product_detail = Product_detail.objects.all()
    curreent_user = request.user
    shopcart = ShopCart.objects.filter(user_id = curreent_user.id)
    total1 =0
    total = 0
    totalship = 15000
    for rs in shopcart:
        total1 += rs.product.price * rs.quantity
    total = total1 + totalship
    extra_context = {
        'product': product,
        'product_laster':product_laster,
        'product_detail': product_detail,
        'shopcart': shopcart,
        'total1': total1,
        'total': total,
    }

    return render(request, 'cart.html', extra_context)            

@login_required(login_url='/login')
def deleteformcart(request, id):
    ShopCart.objects.filter(id=id ).delete()
    messages.success(request,"Đã xóa sản phẩm trong giỏ")
    return HttpResponseRedirect('/shopcart')

def deleteshop(request, id):
    order = Order.objects.get(id=id)
    order.status = "Đã Hủy"
    order.save()
    return HttpResponseRedirect('/order/ordertracking')


def orderproduct(request):
    city = City.objects.all()
    huyen = district.objects.all()
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:10]
    product_detail = Product_detail.objects.all()
    curreent_user = request.user
    profile = UserProfile.objects.get(user_id = curreent_user.id)
    shopcart = ShopCart.objects.filter(user_id = curreent_user.id)
    totalship = 15000
    total = 0
    for rs in shopcart:
        total = total + (rs.product.price * rs.quantity)
    total += totalship
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.first_name = form.cleaned_data['first_name'] 
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.country = form.cleaned_data['country']
            data.ward = form.cleaned_data['ward']
            data.phone = form.cleaned_data['phone']   
            data.user_id = curreent_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(5).upper()
            data.code = ordercode
            data.save()     
            shopcart = ShopCart.objects.filter(user_id = curreent_user.id)  
            for rs in shopcart:
                detail = OrderProduct()
                detail.order_id = data.id
                detail.product_id = rs.product_id
                detail.user_id = curreent_user.id
                detail.quantity = rs.quantity
                detail.price = rs.product.price
                detail.amount = rs.amount
                detail.save()

                product = Product.objects.get(id = rs.product_id)
                product.quantities -= rs.quantity
                product.save()

            ShopCart.objects.filter(user_id = curreent_user.id).delete()
            request.session['cart_item']    = 0
            messages.success(request, "Bạn đã đặt hàng thành công. Chúc bạn một ngày tốt lành !!!")
            return render(request, 'OrderComplete.html', {'ordercode': ordercode, 'product': product,'product': product,  'product_laster':product_laster,    
                        'product_detail': product_detail,})
        else:
            # messages.warning(request, form.errors)
            return HttpResponseRedirect("/order/orderproduct")
    form = OrderForm()
    profile = UserProfile.objects.get(user_id=curreent_user.id) 
    extra_context = {
                        'product': product,
                        'product_laster':product_laster,    
                        'product_detail': product_detail,
                        'shopcart': shopcart,
                        'total': total,
                        'profile': profile,
                        'city': city,
                        'huyen': huyen
                    }
    return render(request, 'checkout.html', extra_context)

# def getdetails(request):
#     country_name = request.GET['cnt']
#     # print "ajax country_name ", country_name

#     result_set = []
#     all_cities = []
#     answer = str(country_name[1:-1])
#     selected_country = City.objects.get(name=answer)
#     # print "selected country name ", selected_country
#     all_cities = selected_country.city_set.all()
#     for city in all_cities:
#         # print "city name", city.name
#         result_set.append({'name': city.name})
#     return HttpResponse(simplejson.dumps(result_set), mimetype='application/json',     content_type='application/json')



def OrderTracking(request):
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:10]
    product_detail = Product_detail.objects.all()
    curreent_user = request.user
    orderproduct = Order.objects.filter(user_id = curreent_user.id)
    extra_context = {
        'product': product,
        'product_laster':product_laster,
        'product_detail': product_detail,
        'orderproduct': orderproduct,
    }
    return render(request, 'ordertracking.html', extra_context)

def orderproductdetail(request, id):
    product = Product.objects.all()
    product_laster = Product_detail.objects.all()
    product_detail = Product_detail.objects.all()
    curreent_user = request.user
    order = Order.objects.get(id = id)
    orderproductdetail = OrderProduct.objects.filter(order_id = id)
    total = 0
    for rs in orderproductdetail:
        total += rs.product.price * rs.quantity

    extra_context = {
        'product': product,
        'product_laster':product_laster,
        'product_detail': product_detail,
        'order': order,
        'orderproductdetail': orderproductdetail,
        'total': total,
    }
    return render(request, 'ordertracking-detail.html', extra_context)
def load_cities(request):
    country_id = request.GET.get('city')
    cities = district.objects.filter(city_id = country_id).order_by('name')
    return render(request, 'city_dropdown_list_options.html',{'cities': cities})

def load_district(request):
    ward_id = request.GET.get('district')
    districts = ward.objects.filter(district_id = ward_id).order_by('name')
    return render(request, 'country_dropdown_list_options.html',{'districts': districts})

def OrderCancel(request):
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:10]
    product_detail = Product_detail.objects.all()
    curreent_user = request.user
    orderproduct = Order.objects.filter(user_id = curreent_user.id)
    extra_context = {
        'product': product,
        'product_laster':product_laster,
        'product_detail': product_detail,
        'orderproduct': orderproduct,
    }
    return render(request, 'ordercancel.html', extra_context)