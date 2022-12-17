from django.urls import path
from . import views
from django.urls import re_path as url

urlpatterns = [
    # This url is a main page which display all available products
    path('products/', views.main, name='all_available_products'),

    # This url is a category page which display all available products in a category
    path('products/<str:category_slug>/', views.main, name='all_available_category'),

    # This url is a detail category which display detail about available product
    path('products/<int:id>/<slug:slug>/', views.main_detail, name='product_details'),
]

