from rest_framework import serializers
from product.models import Products, Category
from product.serializers.category_serializers import CategorySerializers

class ProductsSerializers(serializers.ModelSerializer):
    category = CategorySerializers(read_only = True, many = True)
    categories_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only= True, many = True)

    class Meta:
        model = Products
        fields = [
            'title',
            'description',
            'price',
            'ative',
            'category',
            'categories_id'
        ]
    
    def create(self, validated_data):
        category_data = validated_data.pop('categories_id')
        
        products = Products.objects.create(**validated_data)

        for category in category_data:
            products.category.add(category)        
            
        return products