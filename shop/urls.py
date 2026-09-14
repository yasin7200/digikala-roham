from django.urls import path
from .import views

urlpatterns = [
    path('products', views.pro_view, name='products')
]