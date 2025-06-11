from rest_framework import serializers
from .models import Proprietaire

class ProprietaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proprietaire
        fields = ['id', 'nom_complet', 'email', 'telephone', 'adresse', 'date_naissance', 
                  'piece_identite', 'date_inscription', 'statut_actif']