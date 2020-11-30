from django.test import TestCase
from django.test import Client
from cinepepe.models import *
import sys
import socket
from django.test.utils import setup_test_environment
import uuid


class test_pelicula_form(TestCase):
    """Comprobamos el acceso a las vistas desde los usuarios creados"""
    def setUp(self):      
        Director.objects.create(uuid = uuid.uuid4(), first_name='Danielle',last_name="Huffman")
        Director.objects.create(uuid = uuid.uuid4(), first_name='Shirley',last_name="Grassi")
        Genre.objects.create(uuid=uuid.uuid4(),name="Terror")
        Genre.objects.create(uuid=uuid.uuid4(),name="Drama")
        Genre.objects.create(uuid=uuid.uuid4(),name="Accion")


    def test_crear_peliculas_y_relaciones(self):
        directores = Director.objects.all()
        
        pelicula1 = Pelicula(uuid=uuid.uuid4(),
                             title="Bastardos sin Gloria",
                             sinopsis="Es el primer año de la ocupación alemana de Francia. El oficial aliado, teniente Aldo Raine, ensambla un equipo de soldados judíos para cometer actos violentos en contra de los nazis, incluyendo la toma de cabelleras. Él y sus hombres unen fuerzas con Bridget von Hammersmark, una actriz alemana y agente encubierto, para derrocar a los líderes del Tercer Reich. Sus destinos convergen con la dueña de teatro Shosanna Dreyfus, quien busca vengar la ejecución de su familia.",
                             imagen="https://images-ext-1.discordapp.net/external/YIY1bjj53YEewvTxAirFPPM5KMLLSZMqIDnoihlDTy4/https/www.wallpapertip.com/wmimgs/74-747560_inglorious-bastards-wallpaper-hd.jpg?width=1160&height=653")
        pelicula1.director = directores[0]
        pelicula1.save()
        generos = Genre.objects.all()

        pelicula1.generos.add(generos.get(name= "Accion"))
        pelicula1.save()

        pelicula2 = Pelicula(uuid=uuid.uuid4(),
                             title = "SAU",
                             sinopsis= "Adam y Lawrence se despiertan encadenados en un baño infecto con un cadáver entre ellos. Su secuestrador es un maniaco, cuyo juego consiste en forzar a sus cautivos a herirse a sí mismos o a otros para permanecer vivos.",
                             imagen = "https://media.discordapp.net/attachments/526783541774647316/782785436719513610/187411.png?width=1160&height=653",
                             )
        pelicula2.director = directores[1]
        pelicula2.save()
        pelicula2.generos.add(generos.get(name = "Terror"))
        pelicula2.save()
