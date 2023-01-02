from django.contrib import admin
from .models import Order, OrderItem, Shipping
from import_export.admin import ExportActionMixin


# This class is connected with class OrderAdmin
# It doesn't display in main admin panel
# It display in 'Orders' cart as a detail information

class OrderItemInline(admin.TabularInline):
    model = OrderItem


# This class display in admin panel as a 'Orders'
# Inherits from class 'OrderItemInLine'
# Display all necessary information
# The button 'sent' says if the order is completed or not
@admin.register(Order)
class OrderAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['sent', 'paid', 'created', 'email']

    list_filter = ['paid', 'created']

    inlines = [OrderItemInline]


@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ['active', 'supplier_name', 'shipping_price']

    list_filter = ['active', 'shipping_price']
