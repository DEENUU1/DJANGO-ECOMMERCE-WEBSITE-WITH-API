from django.test import TestCase
from shop.models import Category, Product

# To test this model use a comment ->
# -> py manage.py test shop.tests.test_models


# This test is checking Category class from shop/models.py
# For this test I got 0.002s and 'OK'

class TestCategoryModel(TestCase):
    def test_model_str(self):
        name = Category.objects.create(name='Testing that model')
        slug = Category.objects.create(slug='testing-that-model')
        self.assertEqual(str(name), 'Testing that model')


# This test is not finished yet

class TestProductModel(TestCase):
    def test_model_str(self):
        name = Product.objects.create(name='Very fast PC for gaming')
        self.assertEqual(str(name), 'Very fast PC for gaming')