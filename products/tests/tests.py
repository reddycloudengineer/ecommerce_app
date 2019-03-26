from django.test import TestCase

# Create your tests here.
from products.models import Products

class ProductTest(TestCase):
    """Test module for products model"""

    def setUp(self):
        Products.objects.create(
            name='product1',price=25
        )

        Products.objects.create(
            name='product2',price=30
        )

        print('Created two products with setup')
    def test_product_name(self):
        product1=Products.objects.get(name='product1')
        product2=Products.objects.get(name='product2')

        self.assertEqual(product1.get_name(),'product1')
        self.assertEqual(product2.get_name(),'product1')
