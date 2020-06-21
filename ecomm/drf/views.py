from rest_framework import viewsets

from ecomm.drf.serializers import ProductModelSerializer
from ecomm.products.models import Product


class ProductApiViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
