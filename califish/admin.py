from django.contrib import admin
from .models import Category, Vendor, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('name',)
    ordering = ('-created_at',)


@admin.register(Vendor)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'email', 'address',)
    list_display_links = ('name',)


@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'vendor', 'picture' )
    list_display_links = ('name',)


