from django.urls import path, include
from .views import CartList, CartDetail, OrderList, OrderDetails

urlpatterns = [
    path('',CartList.as_view(), name='cart-list'),
    path('<int:pk>',CartDetail.as_view(), name='cart-detail'),
    path('order', OrderList.as_view(), name='order-list'),
    path('order/<int:pk>',OrderDetails.as_view(), name='order-detail')
]