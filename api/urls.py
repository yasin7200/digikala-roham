from django.urls import path
from .import views

urlpatterns = [
    path('persons', views.list_person_view, name='person')
    # path('persons', views.list_person_view, name='person')
]