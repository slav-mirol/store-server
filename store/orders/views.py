from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from store.orders.models import Cart, Order, OrderProduct
from store.orders.serializers import CartSerializer, _CartSerializer, OrderSerializer, _OrderSerializer, \
    _FullInfoSerializer, _OrderProductSerializer
from store.products.models import Product


class CreateCart(APIView):

    def post(self, request):
        want = request.data
        serializer = CartSerializer(data=want)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class FullInfo:
    def __init__(self, order=None, products=[]):
        self.order = order
        self.products = products


class CreateOrder(APIView):
    def post(self, request):
        user = request.data
        wanted = Cart.objects.filter(id_user=user['id_user'])
        # products = []
        serializer = OrderSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        for i in wanted:
            OrderProduct.objects.create(id_order=Order.objects.last(),
                                        id_product=Product.objects.get(name=i.id_product))

        order = Order.objects.last()
        order_products = OrderProduct.objects.filter(id_order=order)
        ids = []
        for i in order_products:
            ids.append(i.id_product)
        ans = FullInfo(order, Product.objects.filter(name__in=ids))
        serializer = _FullInfoSerializer(instance=ans)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
