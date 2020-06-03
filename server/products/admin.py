from django.contrib import admin

from .models import Product, ProductImage, Category, Review

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'price', 'slug', 'stock_qty', 'active', 'in_stock')
    list_editable = ('in_stock', 'price',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Review)
