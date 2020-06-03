from django.contrib import admin

from .models import Plan, Product, ProductImage, Category, Review

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('sku', 'name', 'price', 'slug', 'stock_qty', 'active', 'in_stock')
    list_editable = ('in_stock', 'price',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Review)
