from django.urls import path, include
from .view import ProductList,ProductDetail,CategoryList,CategoryDetail

urlpatterns = [
    path('list/', ProductList.as_view(),name='Product-list'),
    path('list/<int:pk>/', ProductDetail.as_view(),name='Product-Detail'),
    path('category/', CategoryList.as_view(),name='Category-list'),
    path('category/<int:pk>/', CategoryDetail.as_view(),name='category-detail')
]