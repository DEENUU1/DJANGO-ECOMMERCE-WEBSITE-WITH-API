from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    # This url is a main page which display all available products
    path("", views.product_list, name="product_list"),
    # This url is to display search result
    path("search/", views.search, name="search"),
    # This url is a detail category which display detail about available product
    path("<int:id>/<slug:slug>/", views.product_detail, name="product_detail"),
    # This url is to display form to rate products
    path("<int:id>/<slug:slug>/rate", views.product_rate, name="product_rate"),
]
