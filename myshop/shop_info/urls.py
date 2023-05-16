from django.urls import path
from .views import AboutView, ShippingView, DocumentsView, FaqView, MainAPI

app_name = "shop_info"

urlpatterns = [
    # This url is to display about page
    path("about/", AboutView.as_view(), name="about_us"),
    # This url is to display shipping info
    path("shipping/", ShippingView.as_view(), name="shipping"),
    # This url is to display all documents
    path("documents", DocumentsView.as_view(), name="all_documents"),
    # This url is to display faq
    path("faq/", FaqView.as_view(), name="faq"),
    # This url is to display admin user all available api
    path("api", MainAPI.as_view(), name="main_api"),
]
