from rest_framework import serializers

from store.orders.models import Cart, Order, OrderProduct
from store.products.serializers import ProductsSerializer


class CartSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Cart
        fields = ('id_user', 'id_product')


class OrderSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = Order
        fields = ('id_user', 'status', 'adress')


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = OrderProduct
        fields = ('id_order', 'id_product', 'quantity')


class _CartSerializer(serializers.Serializer):
    id_user = serializers.CharField()
    id_product = serializers.CharField(max_length=100)

class _OrderSerializer(serializers.Serializer):
    id = serializers.CharField()
    id_user = serializers.CharField()
    adress = serializers.CharField(max_length=1000)
    status = serializers.CharField(max_length=100)

class _OrderProductSerializer(serializers.Serializer):
    id_order = serializers.CharField()
    id_product = serializers.CharField(max_length=100)



class _FullInfoSerializer(serializers.Serializer):
    order = _OrderSerializer()
    products = ProductsSerializer(many=True)
