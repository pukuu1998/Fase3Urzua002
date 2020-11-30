from django.shortcuts import render,redirect
from cinepepe.models import Pelicula, Genre, Director
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
import uuid
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
# para entender esta parte, revisar clase del 14 de octubre minuto 1h 0m 0s
# en este caso, RECORDATORIO, solo se utilizaran 2 para hacer un testeo, no olvidar hacer mas
def index(request):
    num_movies = Pelicula.objects.all()
    num_director = Director.objects.all()

    return render(
        request,
        'index.html',
        context={'num_movies': num_movies, 'num_director': num_director,},
    )


def movies(request):
    peliculas = Pelicula.objects.all()
    num_movies = len(peliculas)
    context = {}
    context['peliculas'] =peliculas
    context['num_movies'] = num_movies 
    return render(request,'cartelera.html',context=context,)

def ver_detalle_pelicula(request,uuid):
    
    pelicula = Pelicula.objects.get(uuid = uuid)
    context = {}
    context['pelicula'] = pelicula

    return render(request,'cinepepe/movie_detail.html',context=context,)

def crear_pelicula(request):
    context = {}
    context['generos'] = Genre.objects.all()
    context['directores'] = Director.objects.all()

    if request.user.is_staff:
        print(request.method)
        if request.method == "POST":
            post = request.POST
            director = Director.objects.get(uuid=post.get('director'))
        
            nueva = Pelicula()
            nueva.uuid = uuid.uuid4()
            nueva.title = post.get('titulo')
            nueva.sinopsis = post.get('sinopsis')
            nueva.save()
            nueva.director = director
            nueva.imagen = post.get('imagen')
            for g in post.getlist('generos'):
                genero = Genre.objects.get(uuid =g)
                nueva.generos.add(genero)
            nueva.save()
            return redirect('/movie/{}'.format(str(nueva.uuid)))
        return render(request,'cinepepe/movie_create.html',context=context,)
    else:
        return HttpResponse(status = 403)

def login_form(request):
    context = {}
    if request.method == "POST":
        post = request.POST
        username = post.get('user')
        password = post.get('password')
        try:
            usuario = User.objects.get(username=username)
            user = authenticate(
                request, username=usuario.username, password=password)
            if user is None:
                return redirect('login')
        except User.DoesNotExist:
            return redirect('login')
        print(user)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request,'cinepepe/login.html',context=context,)


def logout_view(request):
    try:
        if request.user.is_authenticated:
            logout(request)
        else:
            return redirect('/')
        return redirect('/')
    except:
        return('/')
def eliminar_pelicula(request,uuid):
    if request.user.is_authenticated and request.user.is_staff:
        pelicula = Pelicula.objects.get(uuid = uuid)
        pelicula.delete()
        return redirect('/movies')
    else:
        return HttpResponse(status = 403)
        
    return render(request,'cinepepe/login.html',context=context,)
def ver_directores(request):
    context = {}
    directores = Director.objects.all()
    directores = [ d for d in directores]
    #Los ordeno por orden alfabertico de los nombres
    directores.sort(key=lambda x: x.first_name, reverse=False)
    context['directores'] = directores

    return render(request,'cinepepe/view_directors.html',context=context,)

def ver_generos(request):
    context = {}
    generos = Genre.objects.all()
    generos = [ g for g in generos]
    generos.sort(key=lambda x: x.name, reverse=False)
    context['generos'] = generos
    
    return render(request,'cinepepe/view_genres.html',context=context,)
    
def crear_director(request):
    context = {}
    if request.user.is_staff:
        print(request.method)
        if request.method == "POST":
            post = request.POST

            n = Director()
            n.uuid = uuid.uuid4()
            n.first_name = post.get('first_name')
            n.last_name = post.get('last_name')
            n.save()
            
            return redirect('/directors')
        return render(request,'cinepepe/director_create.html',context=context,)
    else:
        return HttpResponse(status = 403)

def eliminar_director(request,uuid):
    if request.user.is_authenticated and request.user.is_staff:
        director = Director.objects.get(uuid = uuid)
        director.delete()
        return redirect('/directors')
    else:
        return HttpResponse(status = 403)

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


