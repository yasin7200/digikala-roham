from django.urls import path
from .import views

urlpatterns = [
    path('products', views.pro_view, name='products'),
    path('products/type/<str:model>/', views.pro_view, name='products_by_type'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('cart-add/<int:pk>', views.add_to_cart, name='cart_add'),
]