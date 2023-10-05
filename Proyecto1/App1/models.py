from django.db import models

class Familia(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    edad = models.IntegerField()

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    edad = models.IntegerField()

    
class Catalogo(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    valor = models.IntegerField()
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.IntegerField()
    
    
class Informacion(models.Model):
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.IntegerField()