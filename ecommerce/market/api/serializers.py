from asyncore import read
from rest_framework import serializers
from market.models import Products,Category
class ProductSerializer(serializers.ModelSerializer):
    category=serializers.CharField(source='category.name')
    uploaded_by=serializers.CharField(source='uploaded_by.username')
    class Meta:
        model = Products
        fields = '__all__'
        
        
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    products=ProductSerializer(many=True,read_only=True)
    class Meta:
        model=Category
        fields = "__all__"
        

class CartProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Products
        exclude = ['description', 'in_stock','uploaded_by','date_created', 'updated']
        
        

class CartOrderProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Products
        exclude = ['description', 'in_stock','uploaded_by','date_created', 'updated', 'ISBN', 'category']
