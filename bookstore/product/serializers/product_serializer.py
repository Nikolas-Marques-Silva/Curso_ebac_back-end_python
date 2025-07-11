from rest_framework import serializers

from product.models.product import Product
from product.serializers.category_serializer import CategorySerializer

from product.models.category import Category


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True, many=True
    )

    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
            "category",
            "active",
            "id",
            "category_id",
        ]

    def create(self, validated_data):
        category_data = validated_data.pop("category_id")
        product = Product.objects.create(**validated_data)
        for category in category_data:
            product.category.add(category)
        return product
