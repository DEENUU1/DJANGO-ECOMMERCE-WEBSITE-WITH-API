from django.test import SimpleTestCase
from django.urls import resolve, reverse
from shopcontact.views import contact


class TestUrls(SimpleTestCase):
    def test_contact_resolve(self):
        url = reverse("contact")
        print(resolve(url))
        self.assertEqual(resolve(url).func, contact)
