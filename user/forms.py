from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from user.models import UserProfile
from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, Textarea,ModelForm
from home.models import City, district, ward
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, label= 'User Name: ')
    email = forms.EmailField(max_length=200, label= 'Email: ')
    first_name = forms.CharField(max_length=100, help_text='First Name', label='First Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name', label='Last Name')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

class EditProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['email','first_name','last_name']

class UserForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone','address','city','country', 'ward' ,'image']
    
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
        
        # super().__init__(*args, **kwargs)
        self.fields['ward'].queryset = ward.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['ward'].queryset = ward.objects.filter(district_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk:
            self.fields['ward'].queryset = self.instance.country.ward.order_by('name')
    
        