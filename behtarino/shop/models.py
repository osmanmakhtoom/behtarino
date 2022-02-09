from django.db import models
from django.contrib.auth.models import User


def getUsersWithGtNOrders(n):
    return User.objects.filter(orders__gt=int(n))


def getProductsOrderOfOrderLinesGtK(k):
    return Product.objects.filter(orderLines__order__gt=int(k))


def getProductsPaidPriceGtN(n):
    return Product.objects.filter(orderLines__price__gt=float(n))


def getProductsPaidQuantityGtN(n):
    return Product.objects.filter(orderLines__quantity__gt=int(n))


class Order(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders",
    )


class OrderLine(models.Model):
    order = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE,
        related_name="lines",
    )
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='orderLines',
    )
    quantity = models.IntegerField()
    price = models.FloatField()

    def save(self, *args, **kwargs):
        self.price = self.quantity * self.product.price
        super(OrderLine, self).save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='products',
    )
    name = models.CharField(
        max_length=255,
    )
    price = models.FloatField()


class Category(models.Model):
    name = models.CharField(
        max_length=255,
    )
