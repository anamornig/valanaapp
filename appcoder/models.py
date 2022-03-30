from django.db import models

# Create your models here.
class Posteo(models.Model):
    
    titulo = models.CharField(max_length=40)
    texto = models.CharField(max_length=400)

class Pais(models.Model):

    nombre = models.CharField(max_length=40)
    continente = models.CharField(max_length=25)
    capital = models.CharField(max_length=40)

class Ciudad(models.Model):

    nombre = models.CharField(max_length=40)
    paisdeorigen = models.CharField(max_length=40)
    codigopostal = models.IntegerField(primary_key=True)
