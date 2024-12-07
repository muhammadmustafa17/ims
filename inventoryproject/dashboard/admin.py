from django.contrib import admin
from  . models import Product
from django.contrib.auth.models import Group


admin.site.site_header = 'StrawHats Inventory Dashboard'



class ProdcutAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity',)
    #list_filter = ('category',)
    list_filter = ['category']

# Register your models here.

admin.site.register(Product, ProdcutAdmin)
#admin.site.unregister(Group)
