from django.db import models
from django.utils import timezone
from ..users.models import User
from ..products.models import Product


class Order(models.Model):
    id_user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    adress = models.CharField(max_length=1000)
    status = models.CharField(max_length=100, default='PENDING')
    date_joined = models.DateTimeField(default=timezone.now)


class OrderProduct(models.Model):
    id_order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name='oreder2order')
    id_product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='order2product')
    quantity = models.PositiveIntegerField(default=0)


class Cart(models.Model):
    id_user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    id_product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
