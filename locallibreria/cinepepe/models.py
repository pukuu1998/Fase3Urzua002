from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances

# Create your models here.

class Genre(models.Model):
	uuid = models.UUIDField()
	name=models.CharField(max_length=100)


	def get_short_uuid(self):
		codigo =str(self.uuid) 
		return codigo[:len(codigo)//3]

		
	def __str__(self):
		return self.name 


class Director(models.Model):

	"""Model representing an author."""

	class Meta:
		db_table = "directores"
		verbose_name = "Director"
		verbose_name_plural = "Directores"
		ordering = ['last_name', 'first_name']

	uuid = models.UUIDField(default=None,null=True)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	def get_absolute_url(self):
		return reverse('director-detail', args=[str(self.id)])

	def get_fullname(self):
		return "{} {}".format(self.last_name,self.first_name)
	
	def get_short_uuid(self):
		codigo =str(self.uuid) 
		return codigo[:len(codigo)//3]
	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.last_name}, {self.first_name}'



class Pelicula(models.Model):
	uuid = models.UUIDField(default=None,null=True)
	title = models.CharField(max_length=200)
	director = models.ForeignKey(Director, on_delete=models.DO_NOTHING, null=True)
	sinopsis = models.TextField(max_length=1000)
	generos = models.ManyToManyField(Genre,blank=True)
	imagen = models.TextField()

	def __str__(self):	
		return self.title
    
	def get_num_generos(self):
		return len(self.generos.all())

	def get_absolute_url(self):
		"""Returns the url to access a detail record for this book."""
		return reverse('book-detail', args=[str(self.id)])