# gestion_immo/views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .models import (
    Maison, Commune, AgenceImmo, TypeDocument, Location,
    PaiementLoyer, Penalite, Commodite, CommoditeMaison, PhotoMaison
)
from .serializers import (
    MaisonSerializer, CommuneSerializer, AgenceImmoSerializer, TypeDocumentSerializer,
    LocationSerializer, PaiementLoyerSerializer, PenaliteSerializer, CommoditeSerializer,
    CommoditeMaisonSerializer, PhotoMaisonSerializer
)

class MaisonViewSet(viewsets.ModelViewSet):
    queryset = Maison.objects.all()
    serializer_class = MaisonSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Maison.objects.filter(sup=False)

class CommuneViewSet(viewsets.ModelViewSet):
    queryset = Commune.objects.all()
    serializer_class = CommuneSerializer
    permission_classes = [AllowAny]

class AgenceImmoViewSet(viewsets.ModelViewSet):
    queryset = AgenceImmo.objects.all()
    serializer_class = AgenceImmoSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return AgenceImmo.objects.filter(sup=False)

class TypeDocumentViewSet(viewsets.ModelViewSet):
    queryset = TypeDocument.objects.all()
    serializer_class = TypeDocumentSerializer
    permission_classes = [AllowAny]

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Location.objects.filter(sup=False)

    @action(detail=True, methods=['post'])
    def cloturer(self, request, pk=None):
        location = self.get_object()
        if location.cloture:
            return Response({'error': 'Location déjà clôturée'}, status=status.HTTP_400_BAD_REQUEST)
        location.cloture = True
        location.save()
        return Response({'message': 'Location clôturée avec succès'}, status=status.HTTP_200_OK)

class PaiementLoyerViewSet(viewsets.ModelViewSet):
    queryset = PaiementLoyer.objects.all()
    serializer_class = PaiementLoyerSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return PaiementLoyer.objects.filter(sup=False)

class PenaliteViewSet(viewsets.ModelViewSet):
    queryset = Penalite.objects.all()
    serializer_class = PenaliteSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Penalite.objects.filter(sup=False)

class CommoditeViewSet(viewsets.ModelViewSet):
    queryset = Commodite.objects.all()
    serializer_class = CommoditeSerializer
    permission_classes = [AllowAny]

class CommoditeMaisonViewSet(viewsets.ModelViewSet):
    queryset = CommoditeMaison.objects.all()
    serializer_class = CommoditeMaisonSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return CommoditeMaison.objects.filter(sup=False)

class PhotoMaisonViewSet(viewsets.ModelViewSet):
    queryset = PhotoMaison.objects.all()
    serializer_class = PhotoMaisonSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return PhotoMaison.objects.filter(sup=False)
