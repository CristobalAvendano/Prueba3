from django.urls import path, include
from .import views


urlpatterns = [
    path('', views.login),
    path('index.html', views.index),
    path('agregar.html', views.agregar),
    path('listar.html', views.listar),
]
