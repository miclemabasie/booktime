from django.test import TestCase
from .models import Product

# Create your tests here.
class TestTestingModels(TestCase):
    def test_model_string_method(self):
        name = Product.objects.create(name="miclem")

        self.assertEqual(str(name), "miclem")
