from django.db import models

# Create your models here.
#Creamos un modelo para el objecto Terreno
class Land(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    base = models.FloatField()
    height = models.FloatField()
    description = models.TextField()
