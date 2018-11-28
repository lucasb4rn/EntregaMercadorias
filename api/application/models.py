from django.db import models

# Create your models here.
class Mapas(models.Model):
    ponto_inicial = models.CharField(max_length=1)
    ponto_final = models.CharField(max_length=1)
    distancia = models.CharField(max_length=10)
