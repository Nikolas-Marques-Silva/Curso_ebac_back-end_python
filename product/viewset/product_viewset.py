from rest_framework.viewsets import ModelViewSet

from product.models import Products
from product.serializers import ProductsSerializers


class ProductViewSet(ModelViewSet):
    serializer_class = ProductsSerializers
    queryset = Products.objects.all().order_by("id")

    def get_queryset(self):
        return super().get_queryset()
