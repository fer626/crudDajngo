from django.db import models
from .models import *
from django.contrib.auth.models import User

# Create your models here.
class Usuarios(models.Model):
	nombre = models.CharField(max_length=40)
	apellidos = models.CharField(max_length=40)
	direccion = models.CharField(max_length=40)
	estatus = models.ForeignKey('gestorusuarios.Estatus', null=True, blank=True, on_delete=models.CASCADE)
	rol = models.ForeignKey('gestorusuarios.Rol', null=True, blank=True, on_delete=models.CASCADE)
	usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	fecha_nacimiento = models.DateField(null=True)
	curp = models.CharField(max_length=18)
	fecha_contratacion = models.DateField(null=False)
	correo = models.EmailField(max_length=254)
	telefono = models.CharField(max_length=12)
	celular = models.CharField(max_length=12)

	def __str__(self):
		return self.nombre + " " + self.apellidos + " - " + self.correo

class Estatus(models.Model):
	nombre = models.CharField(max_length=10)
	def __str__(self):
		return self.nombre

class Rol(models.Model):
	nombre = models.CharField(max_length=20)
	def __str__(self):
		return self.nombre