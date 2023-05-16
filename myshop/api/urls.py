from django.urls import path
from .views import *

app_name = "api_data"

urlpatterns = [
    # This url allows admin user to see all product data
    path("product_list", ProductListView.as_view(), name="data_product"),
    # This url allows admin user to see all category data
    path("data_category", CategoryListView.as_view(), name="data_category"),
    # This url allows admin user to add new products
    path("add_product", AddProductView.as_view(), name="add_product"),
    # This url allows admin user to add new category
    path("add_category", AddCategoryView.as_view(), name="add_category"),
    # This url allows admin user to see all available coupons
    path("data_coupon", CouponListView.as_view(), name="data_coupon"),
    # This url allows admin user to add new coupon
    path("add_coupon", AddCouponView.as_view(), name="add_coupon"),
    # This url allows admin user to see customer information from the order
    path("data_order", OrderListView.as_view(), name="data_order"),
    # This url allows admin user to see order information
    path("data_order_item", OrderItemListView.as_view(), name="data_order_item"),
    # This url allows admin user to see delivery information
    path("data_delivery", DeliveryListView.as_view(), name="data_delivery"),
    # This url allows admin user to add new delivery price
    path("add_delivery", AddDeliveryView.as_view(), name="add_delivery"),
]
