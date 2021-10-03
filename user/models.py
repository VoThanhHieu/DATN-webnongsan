from django.db import models
from home.models import City, district, ward
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, blank=True)
    address = models.CharField(max_length=100,blank=True)
    city=   models.ForeignKey(City,on_delete=models.CASCADE, default=14, blank=True)
    country = models.ForeignKey(district,on_delete=models.CASCADE, default=12, blank=True)
    ward = models.ForeignKey(ward,on_delete=models.CASCADE, default=156, blank=True)
    image = models.ImageField(blank=True,upload_to='image/user', default="static/image/user.png")
    
    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + ' [' + self.user.username + '] '

    def image_tag(self):
        return mark_safe('<img src = "{}"height = "50" />'.format(self.image.url))

    image_tag.short_description = 'Image'