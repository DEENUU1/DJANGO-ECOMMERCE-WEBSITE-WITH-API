from django.test import TestCase
from shop.models import Category, Product
from django.urls import reverse

# To test this model use a comment ->
# -> coverage run manage.py test shop.tests.test_models


# This test is checking Category class from shop/models.py
# It is checking does the program correctly returns:
# self.name as a string
# and absolute url

class TestCategoryModel(TestCase):
    def test_model_str(self):
        name = Category.objects.create(name='Testing that model')
        slug = Category.objects.create(slug='testing-that-model')
        self.assertEqual(str(name), 'Testing that model')

    def test_absolute_url(self):
        product = Category.objects.create(name='Testing that model',
                                         slug='testing-that-model')
        url = product.get_absolute_url()
        excepted_url = reverse('shop:product_list_by_category',
                               args=[product.slug])
        self.assertEqual(url, excepted_url)

