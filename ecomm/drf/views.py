from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import generics

from ecomm.drf.serializers import ProductModelSerializer, CategoryModelSerializer
from ecomm.products.models import Product, Category


class ProductAPIViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer


class CategoryListOnlyAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
