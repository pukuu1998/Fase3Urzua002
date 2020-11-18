from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cartelera/', views.cartelera, name='cartelera'),
    
]