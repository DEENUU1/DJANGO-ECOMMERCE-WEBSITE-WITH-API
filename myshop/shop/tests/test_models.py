from django.test import TestCase
from shop.models import Category


class TestCategoryModel(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(
            name="klawiatury",
            slug="klawiatury",
        )

    def test_name_slug(self):
        self.assertEqual(self.category1.slug, "klawiatury")

    def test_name_str(self):
        self.assertEqual(self.category1.name, "klawiatury")
