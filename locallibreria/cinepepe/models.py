from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances

# Create your models here.

class Genre(models.Model):
	name=models.CharField(max_length=100)

	def __str__(self):
		return self.name 

class Pelicula(models.Model):
	title=models.CharField(max_length=200)
	director=models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
	sinopsis=models.TextField(max_length=1000)
	genre=models.ManyToManyField(Genre)

	def __str__(self):	
		return self.title
    
	def get_absolute_url(self):
		"""Returns the url to access a detail record for this book."""
		return reverse('book-detail', args=[str(self.id)])

#class BookInstance(models.Model):
#	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
#	book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
#	imprint = models.CharField(max_length=200)
#	due_back = models.DateField(null=True, blank=True)
#
#	LOAN_STATUS = (
#		('m', 'Maintenance'),
#		('o', 'On loan'),
#		('a', 'Available'),
#		('r', 'Reserved'),
#	)

#	status = models.CharField(
#		max_length=1,
#		choices=LOAN_STATUS,
#		blank=True,
#		default='m',
#		help_text='Book availability',
#	)

#	class Meta:
#		ordering = ['due_back']
#
#	def __str__(self):
#		"""String for representing the Model object."""
#		return f'{self.id} ({self.book.title})'


class Director(models.Model):
	"""Model representing an author."""
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)

	class Meta:
		ordering = ['last_name', 'first_name']

	def get_absolute_url(self):
		return reverse('director-detail', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.last_name}, {self.first_name}'