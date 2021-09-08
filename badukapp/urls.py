from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create_map, name='create_map'),
    path('', views.home, name='home'),
]
