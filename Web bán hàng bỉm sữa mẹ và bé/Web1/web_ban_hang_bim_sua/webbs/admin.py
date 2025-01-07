from django.contrib import admin
from .models import Category, Product, Customer, Cart, Order, OrderItem, CartItem

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'created_at', 'updated_at')
    search_fields = ('name', 'category__name', 'brand')
    list_filter = ('category', 'brand')
    prepopulated_fields = {'slug': ('name',)}

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'order_date', 'status', 'total_amount', 'payment_status')
    list_filter = ('status', 'payment_status')
    search_fields = ('customer__user__username', 'customer__user__email')

# Register your models here.
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(CartItem)