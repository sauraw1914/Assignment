from django.contrib import admin
from .models import *

from .models import Product

# Register your models here.


class myProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'price','created_at','updated_at')
    search_fields = ('name','weight','price')
    readonly_fields = ('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(Product, myProductAdmin)