from django.shortcuts import render
from rest_framework import viewsets
from .models import Source, PhysicalDataSet
from .serializers import SourceSerializer, PhysicalDataSetSerializer

class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

class PhysicalDataSetViewSet(viewsets.ModelViewSet):
    queryset = PhysicalDataSet.objects.all()
    serializer_class = PhysicalDataSetSerializer


# Create your views here.
