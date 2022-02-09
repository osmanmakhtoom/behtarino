from django.db import models
from django.contrib.auth.models import User


# تابعی برای بدست آوردن لیست کاربرانی که بیشتر از n  خرید داشته اند
def getUsersWithGtNOrders(n):
    return User.objects.filter(orders__gt=int(n))


# تابعی برای بدست آوردن لیست محصولاتی که بیشتر از k  بار در سبد خرید قرار گرفته اند
def getProductsOrderOfOrderLinesGtK(k):
    return Product.objects.filter(orderLines__order__gt=int(k))


# تابعی برای بدست آوردن لیست محصولاتی که قیمت فروش آنها بیشتر از n بوده است
def getProductsPaidPriceGtN(n):
    return Product.objects.filter(orderLines__price__gt=float(n))


# تابعی برای بدست آوردن لیست محصولاتی که تعداد فروش آنها بیشتر از n بوده است
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
    price = models.DecimalField(max_digits=20, decimal_places=3)

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
    price = models.DecimalField(max_digits=20, decimal_places=3)


class Category(models.Model):
    name = models.CharField(
        max_length=255,
    )
