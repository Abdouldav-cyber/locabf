from rest_framework import serializers
from .models import Agence

class AgenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agence
        fields = ['id', 'nom', 'adresse', 'email', 'telephone', 'siret', 'date_creation', 'logo']