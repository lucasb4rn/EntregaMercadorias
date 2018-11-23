from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import MalhaLogistica

# Serializers define the API representation.
class MalhaLogisticaSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('nome', 'ponto_inicial', 'ponto_final', 'distancia')