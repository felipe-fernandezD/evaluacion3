from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Tareas
from .serializers import TareasSerializer
# Create your views here.

class TareasViewSet(viewsets.ModelViewSet):
    queryset = Tareas.objects.all().order_by('-created_at')
    serializer_class = TareasSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['titulo', 'hecho']
    ordering_fields = ['created_at', 'titulo']