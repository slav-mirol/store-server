from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from store.orders.models import Cart, Order, OrderProduct
from store.orders.serializers import CartSerializer, _CartSerializer, OrderSerializer, _OrderSerializer, \
    _FullInfoSerializer, _OrderProductSerializer
from store.products.models import Product
from store.products.serializers import ProductsSerializer


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
        Cart.objects.filter(id_user=user['id_user']).delete()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class GetUsersCart(APIView):
    def get(self, request, user):
        #user = request.GET.get("user")
        query = Cart.objects.filter(id_user=user)
        ans_products = []
        for i in query:
            ans_products.append(Product.objects.get(name=i.id_product))

        serializer = ProductsSerializer(instance=ans_products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetUsersOrders(APIView):
    def get(self, request, user):
        #user = request.GET.get("user")
        query = Order.objects.filter(id_user=user)
        ans = []
        for order in query:
            order_products = OrderProduct.objects.filter(id_order=order)
            ids = []
            for i in order_products:
                ids.append(i.id_product)
            ans.append(FullInfo(order, Product.objects.filter(name__in=ids)))
        serializer = _FullInfoSerializer(instance=ans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChangeOrderStatus(APIView):
    def post(self, request):
        data = request.data
        cur_order = Order.objects.get(id=data['id_order'])
        cur_order.status = data['new_status']
        cur_order.save()
        order_products = OrderProduct.objects.filter(id_order=cur_order.id)
        ids = []
        for i in order_products:
            ids.append(i.id_product)
        ans = FullInfo(cur_order, Product.objects.filter(name__in=ids))
        serializer = _FullInfoSerializer(instance=ans)
        return Response(serializer.data, status=status.HTTP_200_OK)
