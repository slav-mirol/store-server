from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, ProductCategory
from .serializers import ProductSerializer, CategorySerializer, ProductCategorySerializer, ProductsSerializer


def index(request):
    return HttpResponse('BYE FELICIA')


class CreateProductCategoryAPIView(APIView):

    def post(self, request):
        categories = request.data
        for category in categories:
            serializer = ProductCategorySerializer(data=category)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateProductAPIView(APIView):

    def post(self, request):
        products = request.data
        for product in products:
            serializer = ProductSerializer(data=product)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ShowAllCategories(APIView):
    def get(self, request):
        categories = ProductCategory.objects.all()
        serializer = CategorySerializer(instance=categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ShowAllProducts(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductsSerializer(instance=products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ShowProductsFromCategory(APIView):

    def get(self, request):
        category = request.data
        query = Product.objects.filter(category_id=category["id"])
        serializer = ProductsSerializer(instance=query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
