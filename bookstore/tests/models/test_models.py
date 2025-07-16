import pytest

from django.test import Client
from product.models import Category, Products
from order.factories import OrderFactory

@pytest.mark.django_db
def tests_model():
    client = Client()
    test_category = Category.objects.create(
        title = 'Teste category 1',
        slug = 'My category 1',
        ative = True
    )

    product = Products.objects.create(
        title = 'Product 1',
        description = 'Teste product',
        price = 5,
        ative = True
    )

    expected_value_category = "Teste category 1"
    expected_value_product  = "Product 1"  

    assert str(test_category.title) == expected_value_category
    assert str(product.title) == expected_value_product