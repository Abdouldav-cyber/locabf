from rest_framework import serializers
from .models import Maison, Photo
from proprietaire.serializers import ProprietaireSerializer

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'image', 'description']

class MaisonSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    proprietaire = ProprietaireSerializer(read_only=True)

    class Meta:
        model = Maison
        fields = [
            'id', 'proprietaire', 'titre', 'description', 'adresse_complete', 'ville', 
            'code_postal', 'latitude', 'longitude', 'nombre_pieces', 'surface', 
            'type_bien', 'loyer_mensuel', 'charges', 'depot_garantie', 'meuble', 
            'statut', 'date_creation', 'photos'
        ]