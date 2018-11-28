from django.shortcuts import render
from rest_framework import viewsets
from .models import Mapas
from .serializers import MapasSerializer

class MapasViewSet(viewsets.ModelViewSet):

	queryset = Mapas.objects.all()

	serializer_class = MapasSerializer
