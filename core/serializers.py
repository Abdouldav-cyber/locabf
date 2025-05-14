# serializers.py
from rest_framework import serializers
from .models import *

class CommuneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commune
        fields = '__all__'

class PhotoMaisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoMaison
        fields = '__all__'

class CommoditeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commodite
        fields = '__all__'

class CommoditeMaisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommoditeMaison
        fields = '__all__'

class AgenceImmoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgenceImmo
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class MaisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maison
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class PaiementLoyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaiementLoyer
        fields = '__all__'

class PenaliteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Penalite
        fields = '__all__'
