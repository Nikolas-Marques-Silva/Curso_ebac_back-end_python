from rest_framework import serializers

from product.models import Category

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'title',
            'slug',
            'description',
            'ative',
        ]
        extra_kwargs = {'slug': {'required': False}}