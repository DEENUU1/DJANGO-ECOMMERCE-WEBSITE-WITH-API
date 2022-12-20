from django.urls import path
from . import views
from django.urls import re_path as url

app_name = 'shop'

urlpatterns = [
    # This url is a main page which display all available products
    path('', views.product_list, name='product_list'),

    # This url is a category page which display all available products in a category
    path('<str:category_slug>/', views.product_list, name='product_list_by_category'),

    # This url is a detail category which display detail about available product
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

    # This url is for adding comments
    # Doesn't work now
    # path('products/<int:id>/<slug:slug>/comment/', views.add_comment, name='add_comment')
]

