from django.test import TestCase
from django.test import Client
from cinepepe.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import sys
import socket
from django.test.utils import setup_test_environment
import uuid

class test_views(TestCase):
    
    
    @classmethod
    def setUpTestData(cls):
        usuario = User(username="usuario")
        usuario.set_password("pass_usuario")
        usuario.save()
        admin = User(username="admin",is_staff=True,is_superuser=True)
        admin.set_password("pass_admin")
        admin.save()

    def test_vistas_usuario(self):
        vistas = {
                '':200,                
                '/movies':200, #200 esTodo correcto
                '/login':200,
                '/movie/create':403, #403 es acceso denegado                
                '/directors':200,                
                '/director/create':403,                
                '/director/delete/<uuid>':403,                
                '/genres':200,                
                '/movie/delete/<uuid>':403, 
                '/movie/<uuid>':200, 
                '/logout':302, #302 significa que e un redirect              
             }
        for r,s in vistas.items():
            #Testeamos cada vista individualmente
            
            if "<uuid>" not in r:
                usuario = User.objects.get(username="usuario")
                response_login = self.client.login(**{'username':"usuario",'password':'pass_usuario'})
                response = self.client.get(r)
                self.assertEqual(response.status_code,s)
    
    def test_vistas_admin(self):
        vistas = {
                '':200,                
                '/movies':200,
                '/login':200,
                '/movie/create':200,                
                '/directors':200,                
                '/director/create':200,                
                '/director/delete/<uuid>':200,      
                '/genres':200,                
                '/movie/delete/<uuid>':200, 
                '/movie/<uuid>':200, 
                '/logout':302, #302 significa que e un redirect              
             }
        for r,s in vistas.items():
            #Testeamos cada vista individualmente
            
            if "<uuid>" not in r:
                usuario = User.objects.get(username="admin")
                response_login = self.client.login(**{'username':"admin",'password':'pass_admin'})
                response = self.client.get(r)
                self.assertEqual(response.status_code,s)



    