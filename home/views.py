from django.shortcuts import render, redirect
from home.models import Product, Product_detail, Blogcontent, Blogcontent_Single, Comment
from django.contrib.auth.models import User,auth
from home.forms import CommentForm, SearchForm, ExportForm
from order.models import Order
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from home.filters import ProductFilter, ExportFilter, ExportProductFilter
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.
from django.http import Http404, HttpResponse, HttpResponseRedirect
from user.models import UserProfile

def home(request):
    product = Product.objects.all()
    paginator = Paginator(product,12)
    page = request.GET.get('page',1)
    product = paginator.get_page(page)
    product_detail = Product_detail.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:10]
    blogcontent = Blogcontent.objects.all().order_by('date')
    ct = request.session.get('count', 0)
    newcount = ct +1
    request.session['count'] = newcount
    extra_context = {
        'product': product,
        'product_detail': product_detail,
        'product_laster': product_laster,
        'blogcontent':blogcontent,
        'c':newcount
    }
    return render(request, 'index.html', extra_context)

def Index(request):
    product = Product.objects.all()
    paginator = Paginator(product,12)
    page = request.GET.get('page',1)
    product = paginator.get_page(page)
    product_laster = Product_detail.objects.all().order_by('-id')[:10]
    blogcontent = Blogcontent.objects.all().order_by('date')
    ct = request.session.get('count', 0)
    newcount = ct +1
    request.session['count'] = newcount
    extra_context ={
        'product': product,
        'product_laster':product_laster,
        'blogcontent':blogcontent,
        'c':newcount
    }
    return render(request, 'index.html', extra_context)

def search(request):
    query = Product.objects.all()
    product_filter =ProductFilter(request.GET, queryset=query)
    
    extra_context = {
        'form': product_filter.form,
        'product': product_filter.qs,
        'product_laster':product_laster
    }
    return render(request, 'shop.html',extra_context)

def Shop(request):
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:10]
    extra_context ={
        'product': product,
        'product_laster':product_laster
    }
    return render(request, 'shop.html', extra_context)


def shop_product(request, detail_id):
    product = Product.objects.filter(product_detail_id = detail_id )
    product_laster = Product_detail.objects.all().order_by('-id')[:10]
    paginator = Paginator(product,8)
    page = request.GET.get('page',1)
    product = paginator.get_page(page)
    extra_context ={
        'product': product,
        'product_laster':product_laster
    }
    return render(request, 'shop.html', extra_context)

def Login(request):
        product = Product.objects.all()
        product_laster = Product_detail.objects.all().order_by('-id')[:10]
        extra_context ={
            'product': product,
            'product_laster':product_laster
        }
        return render(request, 'login.html', extra_context)

def Checkout(request):
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:10]
    extra_context ={
        'product': product,
        'product_laster':product_laster
    }
    return render(request, 'checkout.html', extra_context)


def Contact(request):
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:10]
    if request.method == 'POST':
        message = request.POST['message']
        send_mail('Liên hệ',message, settings.EMAIL_HOST_USER,['xuantien0113@gmail.com'],fail_silently=False)
        messages.success(request, "Gửi thành công")
    extra_context ={
        'product': product,
        'product_laster':product_laster
    }
    return render(request, 'contact.html', extra_context)

def Blog(request):
    blogcontent = Blogcontent.objects.all().order_by('date')
    product = Product.objects.all()
    paginator = Paginator(product,1)
    page = request.GET.get('page',1)
    product = paginator.get_page(page)
    product_laster = Product_detail.objects.all().order_by('-id')[:10]
    extra_context ={
        'product': product,
        'product_laster':product_laster,
        'blogcontent':blogcontent
    }
    return render(request, 'blog.html', extra_context)

def Blogsingle(request, id):
    blogcontenta = Blogcontent.objects.all().order_by('date')
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:10]
    blogcontent = Blogcontent.objects.get(id = id)
    extra_context ={
        'product': product,
        'blogcontent':blogcontent,
        'blogcontenta':blogcontenta
    }
    return render(request, 'blog-single.html', extra_context)

def shopcart(request):
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:10]
    extra_context ={
        'product': product,
        'product_laster':product_laster
    }
    return render(request, 'cart.html', extra_context)

    
def Help(request):
    return render(request, 'help.html')
def Dathang(request):
    return render(request, 'dathang.html')
def Helphuy(request):
    return render(request, 'helphuy.html')


def About(request):
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:10]
    extra_context ={
        'product': product,
        'product_laster':product_laster
    }
    return render(request, 'about.html', extra_context)

def Productsingle(request, product_id):
    comment = Comment.objects.filter(product_id = product_id)
    product = Product.objects.get(id = product_id)
    product_laster = Product_detail.objects.all().order_by('-id')[:10]
    product_1 = Product.objects.all()
    paginator = Paginator(product_1,8)
    page = request.GET.get('page',1)
    product_1 = paginator.get_page(page)
    extra_context ={
        'product': product,
        'product_1': product_1,
        'product_laster':product_laster,
        'comments': comment
    }
    return render(request, 'product-single.html',extra_context)

def Register(request):
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:10]
    extra_context ={
        'product': product,
        'product_laster':product_laster
    }
    return render(request, 'register.html',extra_context)


def Report(request):
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:10]
    extra_context ={
        'product': product,
        'product_laster':product_laster
    }
    return render(request, 'report.html',extra_context)

def Reportproduct(request):
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:10]
    extra_context ={
        'product': product,
        'product_laster':product_laster
    }
    return render(request, 'report-product.html',extra_context)

def Address(request):
    return render(request, 'address.html')
    
def Update_address(request):
    return render(request, 'update-address.html')

def Search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        product = Product.objects.filter(name__icontains=q)
        extra_context = {'query': q, 'product':product}
        template = 'search.html'
    else:       
        template = 'index.html'
        extra_context = {}
    return render(request, template, extra_context)

def searchreport(request):
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:10]
    order_list = Order.objects.all()
    order_filter = ExportFilter(request.GET, queryset=order_list)
    extra_context ={
        'product': product,
        'product_laster':product_laster,
        'filter': order_filter
    }
    return render(request, 'report.html', extra_context)

def searchreportproduct(request):
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:10]
    product_list = Product.objects.all()
    product_filter = ExportProductFilter(request.GET, queryset=product_list)
    extra_context ={
        'product': product,
        'product_laster':product_laster,
        'filter': product_filter
    }
    return render(request, 'report-product.html', extra_context)
    
@login_required(login_url='/login')
def addcomment(request,id):
    url = request.META.get('HTTP_REFERER')
    # return HttpResponse(url)
    if request.method == 'POST':  # check post
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()  # create relation with model
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.product_id=id
            data.ip = request.META.get('REMOTE_ADDR')
            current_user= request.user
            data.user_id=current_user.id
            data.save()  # save data to table
            return HttpResponseRedirect(url)

    return HttpResponseRedirect(url)
def Information(request):
    curreent_user = request.user
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:10]
    profile = UserProfile.objects.get(user_id=curreent_user.id) 
    extra_context ={
        'profile': profile,
        'product': product,                                 
        'product_laster':product_laster,
    }
    return render(request, 'information.html',extra_context)

def Order_profile(request):
    return render(request, 'order_profile.html')

