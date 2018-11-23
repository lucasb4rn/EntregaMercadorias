from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import serializers
from application.models import Logistica


# Serializers define the API representation.
class LogisticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logistica
        fields = ('nome', 'ponto_inicial', 'ponto_final', 'distancia')