from django.test import SimpleTestCase
from django.urls import resolve, reverse
from cart.views import cart_detail, cart_add, cart_remove


class TestUrls(SimpleTestCase):
    def test_cart_detail_resolve(self):
        url = reverse("cart:cart_detail")
        self.assertEqual(resolve(url).func, cart_detail)

    def test_cart_add_resolve(self):
        url = reverse("cart:cart_add", args=[1])
        self.assertEqual(resolve(url).func, cart_add)

    def test_cart_remove_resolve(self):
        url = reverse("cart:cart_remove", args=[1])
        self.assertEqual(resolve(url).func, cart_remove)
