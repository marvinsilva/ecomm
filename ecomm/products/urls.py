from django.urls import path

from ecomm.products import views

urlpatterns = [
    path('list', views.list_products, name='list'),
    path('create', views.create_product, name='create'),
]
