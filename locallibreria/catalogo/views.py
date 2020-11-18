from django.shortcuts import render
from . models import Genre, Movie, MovieStatus, Director
from django.views import generic

# Create your views here.
def index(request):
    num_Movies = Movie.objects.all().count()
    num_Status = MovieStatus.objects.all().count()

    num_Status_available=MovieStatus.objects.filter(status__exact='a').count()
    num_directors = Director.objects.count()

    return render(
        request,
        'index.html',
        context={'num_books': num_Movies, 'num_instances': num_Status, 
        'num_instances_available': num_Status_available, 'num_authors': num_directors},
    ) 

def cartelera(request):
    num_Movies = Movie.objects.all().count()
    num_Status = MovieStatus.objects.all().count()

    num_Status_available=MovieStatus.objects.filter(status__exact='a').count()
    num_directors = Director.objects.count()

    return render(
        request,
        'cartelera.html',
        context={'num_books': num_Movies, 'num_instances': num_Status, 
        'num_instances_available': num_Status_available, 'num_authors': num_directors},
    ) 