from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('movies/', views.movies, name='movies'),

    path('login',views.login_form,name='login'),

    path('movie/create', views.crear_pelicula, name ="crear_pelicula"),
    
    path('directors',views.ver_directores,name = "view_directors"),
    path('director/create',views.crear_director, name ="create_director"),
    path('director/delete/<uuid>',views.eliminar_director, name ="delete_director"),
    path('genres', views.ver_generos , name = "view_genres"),
    
    path('movie/delete/<uuid>', views.eliminar_pelicula),
    
    path('movie/<uuid>',views.ver_detalle_pelicula),
    
    path('logout',views.logout_view,name="logout"),

]