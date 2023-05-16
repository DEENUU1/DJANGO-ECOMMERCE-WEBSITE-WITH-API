from django.test import SimpleTestCase
from django.urls import resolve, reverse
from order.views import order_create


class TestUrls(SimpleTestCase):
    def test_create_order_resolve(self):
        url = reverse("order:order_create")
        self.assertEqual(resolve(url).func, order_create)
