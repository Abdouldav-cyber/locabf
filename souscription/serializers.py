from rest_framework import serializers
from .models import Souscription
from locataire.serializers import LocataireSerializer
from maison.serializers import MaisonSerializer

class SouscriptionSerializer(serializers.ModelSerializer):
    locataire = LocataireSerializer(read_only=True)
    maison = MaisonSerializer(read_only=True)

    class Meta:
        model = Souscription
        fields = ['id', 'locataire', 'maison', 'date_demande', 'message_locataire', 
                  'statut', 'date_reponse', 'commentaire_agence', 'documents_fournis']