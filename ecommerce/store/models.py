from ipaddress import summarize_address_range
from multiprocessing import AuthenticationError
from unicodedata import category, name
from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=255, blank=True)
    
    
    def __str__(self):
        return self.category_name
    

class Product(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    imagurl = models.URLField(blank=True, null=True)
    price = models.IntegerField()
    summary = models.TextField(blank=True, null=True, max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self):
        return self.title
    
    
    
