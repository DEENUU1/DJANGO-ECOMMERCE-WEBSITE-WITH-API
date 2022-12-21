from django.contrib import admin
from .models import Category, Product
from import_export.admin import ExportActionMixin

# registering model category to admin
# displaying name and slug of the product
@admin.register(Category)
class CategoryAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


# registering model product to admin
# displaying name, slug, price, stock, available, created, update of the product
# available works as a button YES or NO
@admin.register(Product)
class ProductAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock',
                    'available', 'created', 'updated']

    list_filer = ['available', 'created', 'updated']

    list_editable = ['price', 'stock', 'available']

    prepopulated_fields = {'slug': ('name',)}


# This allows administrator in admin panel see all comments
# It should display information like: what product got a comment, subject, main text, user name and user email


# @admin.register(Comments)
# class CommentsAdmin(ExportActionMixin, admin.ModelAdmin):
#     list_display = ['product','subject', 'text', 'user_name', 'email']
