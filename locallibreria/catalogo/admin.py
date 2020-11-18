from django.contrib import admin

# Register your models here.
from . models import Genre, Movie, Director, MovieStatus

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(MovieStatus)