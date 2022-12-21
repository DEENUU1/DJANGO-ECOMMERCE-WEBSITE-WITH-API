from django.test import TestCase
from shopcontact.models import Contact

# To test this model use a comment ->
# -> coverage run manage.py test shopcontact.tests.test_models


# This test is checking Category class from shopcontact/models.py
# It is testing does the code returns subject as a string

class TestCategoryModel(TestCase):
    def test_model_str(self):
        subject = Contact.objects.create(subject='Testing that model')
        self.assertEqual(str(subject), 'Testing that model')
