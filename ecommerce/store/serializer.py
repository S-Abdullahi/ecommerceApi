from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['category_name']
        

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'
        # exclude = ['id']        

class CartProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        exclude = ['summary']
        

class CartOrderProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['title','price']
