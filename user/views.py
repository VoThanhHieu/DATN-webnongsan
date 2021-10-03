from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from user.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm   
from home.models import Product, Product_detail, Blogcontent,Blogcontent_Single, City, district, ward
from user.forms import SignUpForm, forms,UserForm ,EditProfileForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return HttpResponse("User app")

def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user = request.user
            userprofile = UserProfile.objects.get(user_id = current_user.id)
            request.session['userimage'] = userprofile.image.url
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            # Return an 'invalid login' error message.
            messages.warning(request,"Tài khoản hoặc mật khẩu không chính xác!")
            return HttpResponseRedirect('/login')

    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:10]
    extra_context ={
        'product': product,
        'product_laster':product_laster,
    }
    return render(request, 'login.html', extra_context)
    

def singup_form(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            #đưa
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "images/user/user.png"
            data.save()
            return HttpResponseRedirect('/')
        else:
            messages.warning(request ,"Nhập thông tin không chính xác"+ str(form.errors))
            return HttpResponseRedirect('/signup')

    form = SignUpForm()

    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:10]
    extra_context ={
        'product': product,
        'product_laster':product_laster
    }
    return render(request, 'register.html', extra_context)

def logout_form(request):
    logout(request)
    return HttpResponseRedirect('/')    

def user_order(request):
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:10]
    current_user = request.user
    orders = Order.objects.filter(user_id= current_user.id)
    extra_context ={
        'product': product,
        'product_laster':product_laster,
        'orders': orders 
    }
    return render(request, 'register.html', extra_context)
    

@login_required(login_url='/login') # Check login 
def user_password(request):
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:10]
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Thay đổi mật khẩu thành công!')
            return HttpResponseRedirect('/user/password')
        else:
            messages.error(request, 'Vui lòng nhập đúng mật khẩu'+ str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        #category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {'form': form })

def userupdate(request):
    city = City.objects.all()
    huyen = district.objects.all()
    phuong = ward.objects.all()
    product = Product.objects.all()
    product_laster = Product_detail.objects.all().order_by('-id')[:10]
    product_detail = Product_detail.objects.all()    
    current_user = request.user
    user = User.objects.get(pk= current_user.id)
    profile = UserProfile.objects.get(user_id = current_user.id)
    extra_context = {
                        'product': product,
                        'product_laster':product_laster,    
                        'product_detail': product_detail,                    
                        'profile': profile,
                        'city': city,
                        'huyen': huyen,
                        'phuong': phuong,
                        'user': user
                    }
    if request.method == 'POST':
        user_form = EditProfileForm(request.POST, instance=request.user)
        form = UserForm(request.POST, request.FILES)
        if form.is_valid() and user_form.is_valid():
            profile.phone = form.cleaned_data['phone']
            profile.address = form.cleaned_data['address']
            profile.city = form.cleaned_data['city']
            profile.country = form.cleaned_data['country']
            profile.ward = form.cleaned_data['ward']
            profile.image = form.cleaned_data['image']
            profile.save()
            user.first_name = user_form.cleaned_data['first_name']
            user.last_name = user_form.cleaned_data['last_name']
            user.save()
            return render(request, "information.html",extra_context)
        else:
            return HttpResponseRedirect("/user/userupdate", extra_context)
    else:
        form = UserForm()
        user_form = EditProfileForm(instance=request.user)    
    extra_context1 = {
                        'product': product,
                        'product_laster':product_laster,    
                        'product_detail': product_detail,                    
                        'profile': profile,
                        'city': city,
                        'huyen': huyen,
                        'phuong': phuong,
                        'form':form , 
                        'user': user,
                        'user_form':user_form
                    }
    return render(request, 'order_profile.html', extra_context1)