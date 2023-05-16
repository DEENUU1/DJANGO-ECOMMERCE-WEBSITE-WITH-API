from django.urls import path
from . import views


app_name = "order"

urlpatterns = [
    # This url represent completing order
    path("create/", views.order_create, name="order_create"),
]
