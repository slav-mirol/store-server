from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, ProductCategory

def index(request):
    return HttpResponse('BYE FELICIA')


def create(request):
    data = ['обувь', 'штаны', 'верхняя одежда']
    for i in data:
        category, created = ProductCategory.objects.get_or_create(name=i, description='категория одежды')
    return HttpResponse('')