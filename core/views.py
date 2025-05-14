from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import viewsets
from .models import *
from .serializers import *

class CommuneViewSet(viewsets.ModelViewSet):
    queryset = Commune.objects.all()
    serializer_class = CommuneSerializer

class PhotoMaisonViewSet(viewsets.ModelViewSet):
    queryset = PhotoMaison.objects.all()
    serializer_class = PhotoMaisonSerializer

class CommoditeViewSet(viewsets.ModelViewSet):
    queryset = Commodite.objects.all()
    serializer_class = CommoditeSerializer

class CommoditeMaisonViewSet(viewsets.ModelViewSet):
    queryset = CommoditeMaison.objects.all()
    serializer_class = CommoditeMaisonSerializer

class AgenceImmoViewSet(viewsets.ModelViewSet):
    queryset = AgenceImmo.objects.all()
    serializer_class = AgenceImmoSerializer

class MaisonViewSet(viewsets.ModelViewSet):
    queryset = Maison.objects.all()
    serializer_class = MaisonSerializer

class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class PaiementLoyerViewSet(viewsets.ModelViewSet):
    queryset = PaiementLoyer.objects.all()
    serializer_class = PaiementLoyerSerializer

class PenaliteViewSet(viewsets.ModelViewSet):
    queryset = Penalite.objects.all()
    serializer_class = PenaliteSerializer
