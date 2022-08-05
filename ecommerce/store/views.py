from msilib.schema import ServiceInstall
from django.shortcuts import render

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import CategorySerializer, ProductSerializer
from .models import Product, Category

# Create your views here.
class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        category = self.request.query_params.get('category',None)
        return Product.objects.filter(category__category_name=category)




