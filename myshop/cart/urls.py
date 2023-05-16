from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    # This url represent main side of cart
    # In that url user can use all functions of cart
    path("", views.cart_detail, name="cart_detail"),
    # This url doesn't have template
    # It's display in product detail to add product to cart
    path("add/<int:product_id>/", views.cart_add, name="cart_add"),
    # This url doesn't have template
    # It's display in cart to allow user delete product from cart
    path("remove/<int:product_id>/", views.cart_remove, name="cart_remove"),
]
