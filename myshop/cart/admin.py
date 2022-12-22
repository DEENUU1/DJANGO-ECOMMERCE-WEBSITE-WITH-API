from django.contrib import admin
from .models import Order, OrderItem
from import_export.admin import ExportActionMixin


@admin.register(OrderItem)
class OrderItemAdmin(ExportActionMixin, admin.ModelAdmin):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email',
                    'address', 'city', 'postal_code',
                    'created', 'paid']

    list_filter = ['paid', 'created']

    inline = [OrderItemAdmin]

