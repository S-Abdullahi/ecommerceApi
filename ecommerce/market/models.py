from datetime import datetime
from email.policy import default
from tabnanny import verbose
from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=255, unique=True)


    
    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])
    

    class Meta:
        verbose_name_plural='Categories'

    
    
    def __str__(self):
        return self.name

    
    
def upload_location(instance,filename):
    ext=filename.split('.')[-1]
    return "%s/%s.%s" %("img", datetime.now(),ext) 

class Products(models.Model):
    category=models.ForeignKey(Category, related_name='products',on_delete=models.PROTECT,null=True, blank=True) 
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=250)
    image=models.ImageField(null=True,blank=True, upload_to=upload_location)
    ISBN=models.CharField(max_length=13, null=True, blank=True)
    description=models.TextField() 
    price=models.DecimalField(max_digits=6, decimal_places=2) 
    in_stock=models.BooleanField(default=True) 
    slug=models.SlugField(max_length=255, unique=True)
    uploaded_by=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    date_created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    
    class Meta:
        ordering=('date_created',)
        verbose_name_plural='Products'
        
    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])

        
    def __str__(self):
        return self.title +  ' | '  + self.author
 