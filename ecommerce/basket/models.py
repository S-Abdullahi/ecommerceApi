# from django.conf import _DjangoConfLazyObject
from statistics import mode
from django.db import models
from store.models import Product

# Create your models here.
class Cart(models.Model):
    books = models.ManyToManyField(Product, blank=True, related_name='books')
    date_created = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField(null=True, blank=True)
    


class Order(models.Model):
    order_id = models.OneToOneField(Cart,blank=True,related_name='orders', on_delete=models.CASCADE, null=True)
    shipping_address = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null= True, blank=True)
    total_price = models.IntegerField(null=True, blank=True)

    # def __str__(self):
    #     return self.order_id
    