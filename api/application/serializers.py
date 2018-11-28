from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import serializers
from application.models import Mapas


# Serializers define the API representation.
class MapasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mapas
        fields = ('ponto_inicial', 'ponto_final', 'distancia')
