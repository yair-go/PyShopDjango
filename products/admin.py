from django.contrib import admin
from .models import Product, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email')


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
