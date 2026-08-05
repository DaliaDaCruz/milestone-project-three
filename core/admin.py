from django.contrib import admin
from .models import Machine, Booking, Product, Order, OrderItem


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'badge', 'created_at')
    list_filter = ('category', 'badge')
    search_fields = ('name',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'service', 'created_at')
    list_filter = ('service',)
    search_fields = ('name', 'email')


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('price',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_number', 'full_name', 'email', 'total_price', 'created_at'
    )
    list_filter = ('created_at',)
    search_fields = ('order_number', 'full_name', 'email')
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'machine', 'price', 'quantity')
    readonly_fields = ('price',)