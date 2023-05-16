from django.test import SimpleTestCase
from django.urls import resolve, reverse
from coupons.views import coupon_apply


class TestUrls(SimpleTestCase):
    def test_coupon_apply_resolve(self):
        url = reverse("coupons:apply")
        self.assertEqual(resolve(url).func, coupon_apply)
