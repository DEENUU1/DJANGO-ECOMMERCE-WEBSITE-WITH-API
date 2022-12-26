from django.contrib import admin
from .models import Order, OrderItem
from import_export.admin import ExportActionMixin

# This class display all ordered items in admin panel

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ['product', 'quantity', 'price']

@admin.register(Order)
class OrderAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email',
                    'address', 'city', 'postal_code',
                    'created', 'paid']

    list_filter = ['paid', 'created']

    inlines = [OrderItemInline]



