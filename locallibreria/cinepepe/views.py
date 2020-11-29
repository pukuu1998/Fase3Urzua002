from django.shortcuts import render
from . models import Pelicula, Genre, Director
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.
# para entender esta parte, revisar clase del 14 de octubre minuto 1h 0m 0s
# en este caso, RECORDATORIO, solo se utilizaran 2 para hacer un testeo, no olvidar hacer mas
def index(request):
    num_movies = Pelicula.objects.all().count()

    num_director = Director.objects.count()

    return render(
        request,
        'index.html',
        context={'num_movies': num_movies, 'num_director': num_director,},
    )


def movies(request):
    num_movies=Pelicula.objects.all()
    
    return render(
        request,
        'movies.html',
        context={'num_movies':num_movies},
    )



class GenreCreate(CreateView):
    model = Genre
    fields = '__all__'

class GenreUpdate(UpdateView):
    model = Genre
    fields = '__all__'

class GenreDelete(DeleteView):
    model = Genre
    success_url = reverse_lazy('index')

class GenreDetailView(generic.DetailView):
    model = Genre



class MovieCreate(CreateView):
    model = Pelicula
    fields = '__all__'

class MovieUpdate(UpdateView):
    model = Pelicula
    fields = '__all__'

class MovieDelete(DeleteView):
    model = Pelicula
    success_url = reverse_lazy('index')

class MovieDetailView(generic.DetailView):
    model = Pelicula



class DirectorCreate(CreateView):
    model = Director
    fields = '__all__'

class DirectorUpdate(UpdateView):
    model = Director
    fields = '__all__'

class DirectorDelete(DeleteView):
    model = Director
    success_url = reverse_lazy('index')

class DirectorDetailView(generic.DetailView):
    model = Director


