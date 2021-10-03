

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    pass

@admin.register(City)
class CitytAdmin(ImportExportModelAdmin):
    pass
@admin.register(district)
class districtAdmin(ImportExportModelAdmin):
    pass
@admin.register(ward)
class wardAdmin(ImportExportModelAdmin):
    pass

@admin.register(Product_detail)
class ProductdetailAdmin(ImportExportModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment',]
    list_filter = ['rate',]

admin.site.register(Customer)
# admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
# admin.site.register(Product_detail)
admin.site.register(Blogcontent)
admin.site.register(Blogcontent_Single)
admin.site.register(Comment,CommentAdmin)
# admin.site.register(City)
# admin.site.register(district)
# admin.site.register(ward)
admin.site.register(Product_NCC)
admin.site.site_header ='Admin Nông Sản Sạch'
