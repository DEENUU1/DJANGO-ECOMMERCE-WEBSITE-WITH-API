from django.contrib import admin
from .models import Category, Product, ProductRate, Delivery
from import_export.admin import ExportActionMixin


# registering model category to admin
# displaying name and slug of the product
@admin.register(Category)
class CategoryAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


# registering model product to admin
# displaying name, slug, price, stock, available, created, update of the product
# available works as a button YES or NO
@admin.register(Product)
class ProductAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ["name", "slug", "price", "stock", "available", "created", "updated"]

    list_filer = ["available", "created", "updated"]

    list_editable = ["price", "stock", "available"]

    prepopulated_fields = {"slug": ("name",)}


# This class allows admin to display all rates
# Sort them by rate, product and date
@admin.register(ProductRate)
class ProductRateAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ["rate", "product", "date"]

    list_filter = ["rate", "product", "date"]


admin.site.register(Delivery)
