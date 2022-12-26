from django.contrib import admin
from .models import Order, OrderItem
from import_export.admin import ExportActionMixin

# This class allows to display customer and order informations in one page

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ['product', 'quantity', 'price']

# This class display information like: sent, paid, date of created and email in main page
# After clicking on order admin can see all necessary information like: first, last name, email, adress...
@admin.register(Order)
class OrderAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['sent', 'paid', 'created','email']

    list_filter = ['paid', 'created']

    inlines = [OrderItemInline]



