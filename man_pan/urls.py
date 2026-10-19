from django.urls import path
from .import views


urlpatterns = [
    path('', views.manage_view, name='manage'),
    # path('/admin', views.manage_view, name='manage'),
    # path('/support', views.manage_view, name='manage'),
    # path('/accounting', views.manage_view, name='manage'),
]