from django.contrib import admin
from .models import Order, OrderItem
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
    list_display = ["order_status", "paid", "created", "email"]

    list_filter = ["order_status", "created"]

    inlines = [OrderItemInline]
