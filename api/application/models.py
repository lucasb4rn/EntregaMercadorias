from django.db import models

# Create your models here.


class Logistica(models.Model):
	nome = models.CharField(max_length=50)
	ponto_inicial = models.CharField(max_length=1) 
	ponto_final = models.CharField(max_length=1)
	distancia = models.IntegerField()

	def __str__(self):
		return self.nome