from rest_framework import serializers
from .models import Locataire

class LocataireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locataire
        fields = ['id', 'nom_complet', 'email', 'telephone', 'date_naissance', 
                  'profession', 'revenus_mensuels', 'adresse_actuelle', 
                  'date_inscription', 'statut_actif']