from rest_framework.viewsets import ModelViewSet

from product.models import Category
from product.serializers.category_serializers import CategorySerializers


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializers

    def get_queryset(self):
        return Category.objects.all().order_by('id')