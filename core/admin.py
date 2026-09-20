from django.contrib import admin
from .models import Category, Product, ServiceRequest

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'condition')
    list_filter = ('category', 'condition')
    search_fields = ('title', 'description')

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'machine_model', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer_name', 'machine_model', 'issue_description')