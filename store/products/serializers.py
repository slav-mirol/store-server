from rest_framework import serializers
from .models import Product, ProductCategory

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta(object):
        model = ProductCategory
        fields = ('name', 'description')


class ProductSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Product
        fields = ('name', 'description', 'price', 'image', 'quantity', 'category')


class CategorySerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()

class ProductsSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    quantity = serializers.CharField()
    image = serializers.CharField()
    category = serializers.CharField()
