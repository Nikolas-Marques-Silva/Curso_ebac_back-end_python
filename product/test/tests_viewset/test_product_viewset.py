import json

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.urls import reverse

from product.factories import CategoryFactory, ProductsFactory
from order.factories import UserFactory
from product.models import Products

class TestProductViewSet(APITestCase):

    client = APIClient()

    def setUp(self):
        self.user     = UserFactory()
        self.product  = ProductsFactory(title = 'mouse',  price = 100.00)      
        
    def test_get_all_product(self):
        response = self.client.get(
            reverse('product-list', kwargs={'version': 'v1'})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product_data = json.loads(response.content)
        self.assertEqual(product_data['results'][0]['title'], self.product.title)
        self.assertEqual(product_data['results'][0]['price'], self.product.price)

    def test_create_product(self):
        category = CategoryFactory()
        
        data = json.dumps({
            'title': 'notebook',
            'price': 800.00,
            'categories_id': [ category.id ],
        })

        response = self.client.post(
            reverse('product-list', kwargs={'version': 'v1'}),
            data = data, 
            content_type= 'application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        create_product= Products.objects.get(title = 'notebook')

        self.assertEqual(create_product.title, 'notebook')
        self.assertEqual(create_product.price, 800.00)