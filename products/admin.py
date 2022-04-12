from django.contrib import admin
from .models import Product, Category

# Register your models here.

# Code has been used from the Code Institute Boutique Ado
# Walkthrough project


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    """Sorts products by sku"""
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
