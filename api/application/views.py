from django.shortcuts import render
from rest_framework import viewsets
from .models import Logistica
from .serializers import LogisticaSerializer

class LogisticaViewSet(viewsets.ModelViewSet):
	queryset = Logistica.objects.all()
	serializer_class = LogisticaSerializer