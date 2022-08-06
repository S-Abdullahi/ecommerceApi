from market.models import Products,Category
from .serializers import ProductSerializer,CategorySerializer
from rest_framework import generics
from rest_framework import filters
# from store.api.permissions import IsAdminOrReadOnly


class ProductList(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAdminOrReadOnly]
    
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^name', ]
    # permission_classes = [IsAdminOrReadOnly]
    
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer