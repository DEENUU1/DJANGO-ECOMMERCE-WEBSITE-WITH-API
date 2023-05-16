from django.urls import path
from . import views

urlpatterns = [
    # This url is for contact form
    path("contact/", views.contact, name="contact")
]
