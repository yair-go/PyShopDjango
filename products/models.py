from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Order(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_email = models.CharField(max_length=255)
    customer_address = models.CharField(max_length=255)
    order_date = models.DateTimeField()
    shipping_date = models.DateTimeField()
    delivery_date = models.DateTimeField()

