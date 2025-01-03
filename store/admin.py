import uuid
from django.contrib import admin
from .models import Categories, Products, Cart


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('title', 'slug')
    search_fields = ('title',)

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('title', 'price', 'category', 'create_at', 'update_at')
    search_fields = ('title', 'description')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created')
    search_fields = ('user__username', )
