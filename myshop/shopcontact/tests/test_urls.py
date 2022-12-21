from django.test import TestCase
from django.urls import reverse

# This test checks if the main page of the contact form is running

# To run this test write in a console
# coverage run manage.py test shopcontact.tests.test_urls

class UrlTest_HomePage(TestCase):
    def testHomePage(self):
        response = self.client.get('/')
        print(response)

        self.assertEqual(response.status_code, 200)


