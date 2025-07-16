import factory
from faker import Factory as FactoryFaker

from django.contrib.auth.models import User
from product.factories import ProductsFactory

from order.models import Order

faker = FactoryFaker.create()

class UserFactory(factory.django.DjangoModelFactory):
    email       = factory.Faker('pystr')
    username    = factory.Faker('pystr')
    
    class Meta:
        model = User


class OrderFactory(factory.django.DjangoModelFactory):
    user        = factory.SubFactory(UserFactory)
    
    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        if not create:
            return
        
        if extracted: 
            for products in extracted:
                self.products.add(products)
    
    class Meta:
        model = Order