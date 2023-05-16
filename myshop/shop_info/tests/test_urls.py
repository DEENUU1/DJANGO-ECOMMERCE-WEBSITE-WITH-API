from django.test import SimpleTestCase
from django.urls import resolve, reverse
from shop_info.views import AboutView, ShippingView, DocumentsView, FaqView, MainAPI


class TestUrls(SimpleTestCase):
    def test_about_resolve(self):
        url = reverse("shop_info:about_us")
        self.assertEqual(resolve(url).func.view_class, AboutView)

    def test_shipping_resolve(self):
        url = reverse("shop_info:shipping")
        self.assertEqual(resolve(url).func.view_class, ShippingView)

    def test_documents_resolve(self):
        url = reverse("shop_info:all_documents")
        self.assertEqual(resolve(url).func.view_class, DocumentsView)

    def test_faq_resolve(self):
        url = reverse("shop_info:faq")
        self.assertEqual(resolve(url).func.view_class, FaqView)

    def test_main_api_resolve(self):
        url = reverse("shop_info:main_api")
        self.assertEqual(resolve(url).func.view_class, MainAPI)
