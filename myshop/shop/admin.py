from django.contrib import admin
from .models import Category, Product
from import_export.admin import ExportActionMixin

# registering model category to admin
# displaying name and slug of the product
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

# registering model product to admin
# displaying name, slug, price, stock, available, created, update of the product
# available works as a button YES or NO
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock',
                    'available', 'created', 'updated']

    list_filer = ['available', 'created', 'updated']

    list_editable = ['price', 'stock', 'available']

    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)


