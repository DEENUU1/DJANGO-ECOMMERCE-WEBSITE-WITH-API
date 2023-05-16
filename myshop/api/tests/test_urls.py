from django.test import SimpleTestCase
from django.urls import resolve, reverse
from api.views import *


class TestUrls(SimpleTestCase):
    def test_data_product_resolve(self):
        url = reverse("api_data:data_product")
        self.assertEqual(resolve(url).func.view_class, ProductListView)

    def test_data_category_resolve(self):
        url = reverse("api_data:data_category")
        self.assertEqual(resolve(url).func.view_class, CategoryListView)

    def test_add_product_resolve(self):
        url = reverse("api_data:add_product")
        self.assertEqual(resolve(url).func.view_class, AddProductView)

    def test_add_category_resolve(self):
        url = reverse("api_data:add_category")
        self.assertEqual(resolve(url).func.view_class, AddCategoryView)

    def test_data_coupon_resolve(self):
        url = reverse("api_data:data_coupon")
        self.assertEqual(resolve(url).func.view_class, CouponListView)

    def test_add_coupon_resolve(self):
        url = reverse("api_data:add_coupon")
        self.assertEqual(resolve(url).func.view_class, AddCouponView)

    def test_data_order_resolve(self):
        url = reverse("api_data:data_order")
        self.assertEqual(resolve(url).func.view_class, OrderListView)

    def test_data_order_item_resolve(self):
        url = reverse("api_data:data_order_item")
        self.assertEqual(resolve(url).func.view_class, OrderItemListView)

    def test_data_delivery_resolve(self):
        url = reverse("api_data:data_delivery")
        self.assertEqual(resolve(url).func.view_class, DeliveryListView)

    def test_add_delivery_resolve(self):
        url = reverse("api_data:add_delivery")
        self.assertEqual(resolve(url).func.view_class, AddDeliveryView)
