from dataclasses import fields
from importlib.resources import read_binary
from msilib.schema import ServiceInstall
from rest_framework import serializers
from market.api.serializers import CartProductSerializer, CartOrderProductSerializer

from .models import Cart, Order



class CartSerializer(serializers.ModelSerializer):
    
    books = CartProductSerializer(read_only=True,many=True)
    # total_price = books.price
    class Meta:
        model = Cart
        fields = ['id','books','date_created','total_price']
        
class CartOrderSerializer(serializers.ModelSerializer):
    
    books = CartOrderProductSerializer(read_only=True,many=True)
    # total_price = books.price
    class Meta:
        model = Cart
        fields = ['books']
    


class OrderSerializer(serializers.ModelSerializer):
    
    order_id = CartOrderSerializer(read_only=True,many=False)

    class Meta:
        model = Order
        fields = ['id','order_id', 'shipping_address','total_price']
    
