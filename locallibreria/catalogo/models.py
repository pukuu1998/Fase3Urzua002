from django.db import models        #definir modelos
from django.urls import reverse     #direccionar los modelos a urls
import uuid                         #permite reconocer los campos clave de una clase

class Genre(models.Model):
    #Model representing a movie genre."""
	name = models.CharField(max_length=200)
	
	def __str__(self):
		return self.name


class Movie(models.Model):
    
	title = models.CharField(max_length=200)
	director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    
	summary = models.TextField(max_length=1000, help_text='Enter a brief description of the movie')
	genre = models.ManyToManyField(Genre)
    
	def __str__(self):
		return self.title
    
	def get_absolute_url(self):
		"""Returns the url to access a detail record for this movie."""
		return reverse('movie-detail', args=[str(self.id)])


class MovieStatus(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this movie')
	movie = models.ForeignKey('Movie', on_delete=models.SET_NULL, null=True)
	release_date = models.DateField('ReleaseDate', null=True, blank=True)

	LOAN_STATUS = (
		('p', 'Proximamente'),
		('c', 'En Cartelera'),
		('o', 'Out'),
	)

	status = models.CharField(
		max_length=1,
		choices=LOAN_STATUS,
		blank=True,
		default='p',
		help_text='State of the movie',
	)

	class Meta:
		ordering = ['release_date']

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.id} ({self.movie.title})'

    
class Director(models.Model):
	"""Model representing an author."""
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	date_of_birth = models.DateField(null=True, blank=True)
	date_of_death = models.DateField('Died', null=True, blank=True)

	class Meta:
		ordering = ['last_name', 'first_name']

	def get_absolute_url(self):
		return reverse('author-detail', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.last_name}, {self.first_name}'	