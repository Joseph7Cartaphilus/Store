from django.contrib import admin

from .models import ProductCategory, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'short_description', 'price', 'quantity',
                    'category']  # настройка отображения
    list_per_page = 5  # Пагинация


@admin.register(ProductCategory)
class ProductCategory(admin.ModelAdmin):
    list_display = ['name', 'description'] # настройка отображения
    list_per_page = 5  # Пагинация

