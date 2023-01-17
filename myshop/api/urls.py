from django.urls import path
from . import views

app_name = 'api_data'

urlpatterns = [
    # This url allows admin user to see all product data
    path('data_product', views.get_product_data, name='data_product'),

    # This url allows admin user to see all category data
    path('data_category', views.get_category_data, name='data_category'),

    # This url allows admin user to add new products
    path('add_product', views.add_product, name='add_product'),

    # This url allows admin user to add new category
    path('add_category', views.add_category, name='add_category'),

    # This url allows admin user to see all available coupons
    path('data_coupon', views.get_coupon_data, name='data_coupon'),

    # This url allows admin user to add new coupon
    path('add_coupon', views.add_coupon, name='add_coupon'),

    # This url allows admin user to see customer information from the order
    path('data_order', views.get_order_data, name='data_order'),

    # This url allows admin user to see order information
    path('data_order_item', views.get_orderItem_data, name='data_order_item'),

]