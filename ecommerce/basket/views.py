from msilib.schema import ServiceInstall
from django.shortcuts import render

from .serializer import CartSerializer, OrderSerializer
from .models import Cart, Order

from rest_framework import generics
from rest_framework.response import Response


# Create your views here.

class CartList(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = CartSerializer(queryset)
    #     return Response(serializer.data)
    

class CartDetail(generics.RetrieveUpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    

class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetails(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    

