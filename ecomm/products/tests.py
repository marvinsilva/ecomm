from django.test import TestCase

from ecomm.products.models import Product, Category


class ProductStrTestCase(TestCase):
    def test_str_should_return_name(self):
        category = Category.objects.create(name='Teste categoria', description='Teste description', )
        product = Product.objects.create(
            name='Teste Produto',
            description='Teste description',
            category=category,
            price=10.5
        )

        self.assertEqual(str(product), 'Teste Produto')
