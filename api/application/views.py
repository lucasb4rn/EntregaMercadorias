from django.shortcuts import render
from rest_framework import viewsets
from .model import MalhaLogistica

class MalhaLogisticaViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	seralizer_class = UserSerializer