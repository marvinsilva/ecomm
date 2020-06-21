from django.urls import path, include
from rest_framework import routers
from ecomm.drf import views

router = routers.DefaultRouter()
router.register('products', views.ProductAPIViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('categories/', views.CategoryListOnlyAPIView.as_view())
]
