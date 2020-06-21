from django.urls import path

from ecomm.products import views

urlpatterns = [
    path('', views.list_products, name='list'),
]