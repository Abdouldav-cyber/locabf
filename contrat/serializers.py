from rest_framework import serializers
from .models import Contrat
from proprietaire.serializers import ProprietaireSerializer
from locataire.serializers import LocataireSerializer
from maison.serializers import MaisonSerializer
from souscription.serializers import SouscriptionSerializer

class ContratSerializer(serializers.ModelSerializer):
       proprietaire = ProprietaireSerializer(read_only=True)
       locataire = LocataireSerializer(read_only=True)
       maison = MaisonSerializer(read_only=True)
       souscription = SouscriptionSerializer(read_only=True, allow_null=True)

       class Meta:
           model = Contrat
           fields = [
               'id', 'maison', 'locataire', 'proprietaire', 'souscription',
               'date_debut', 'date_fin', 'loyer_mensuel', 'charges_mensuelles',
               'depot_garantie', 'statut', 'document_contrat', 'conditions_particulieres'
           ]