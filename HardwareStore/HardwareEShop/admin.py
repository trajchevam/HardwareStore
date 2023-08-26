from django.contrib import admin
from .models import Cart, CartItem, Product, Brand, Category
# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', ]

admin.site.register(Brand, BrandAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', ]

admin.site.register(Product, ProductAdmin)

class CartAdmin(admin.ModelAdmin):
    list_display = ['user', ]

admin.site.register(Cart, CartAdmin)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', ]

admin.site.register(CartItem, CartItemAdmin)
