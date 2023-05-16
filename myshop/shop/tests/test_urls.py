from django.test import SimpleTestCase
from django.urls import resolve, reverse
from shop.views import product_list, search, product_detail, product_rate


class TestUrls(SimpleTestCase):
    def test_product_list_resolved(self):
        url = reverse("shop:product_list")
        print(resolve(url))
        self.assertEqual(resolve(url).func, product_list)

    def test_search_resolved(self):
        url = reverse("shop:search")
        print(resolve(url))
        self.assertEqual(resolve(url).func, search)

    def test_product_detail_resolved(self):
        url = reverse("shop:product_detail", args=[1, "example-slug"])
        print(resolve(url))
        self.assertEqual(resolve(url).func, product_detail)

    def test_product_detail_resolved2(self):
        url = reverse("shop:product_detail", kwargs={"id": 1, "slug": "example-slug"})
        print(resolve(url))
        self.assertEqual(resolve(url).func, product_detail)

    def test_product_rate_resolved(self):
        url = reverse("shop:product_rate", args=[1, "example-slug"])
        print(resolve(url))
        self.assertEqual(resolve(url).func, product_rate)
