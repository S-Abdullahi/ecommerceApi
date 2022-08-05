from django.urls import path, include
from .views import ProductView, ProductDetailView,CategoryView, CategoryDetailView

urlpatterns = [
    path('',ProductView.as_view(),name='product-list'),
    path('category',CategoryView.as_view(),name='category-list'),
    path('<int:pk>',ProductDetailView.as_view(),name='product-detail'),
    path( 'category-content',CategoryDetailView.as_view(),name='category-detail'),
    
]
