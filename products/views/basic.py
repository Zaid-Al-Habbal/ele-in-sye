from rest_framework import generics
from rest_framework.viewsets import ModelViewSet,
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from products.models import Product
from products.serializers import *


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductViewSet():
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Associate current user as seller automatically
        serializer.save(seller=self.request.user)