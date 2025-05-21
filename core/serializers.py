from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer  # Ajout pour JWT
from django.contrib.auth import authenticate  # Ajout pour authentification
from .models import Maison, Commune, AgenceImmo, Document, Location, PaiementLoyer, Penalite, Commodite, CommoditeMaison, PhotoMaison

# Sérialiseur personnalisé pour utiliser email au lieu de username
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'] = serializers.EmailField(required=True)
        self.fields.pop('username', None)  # Supprime le champ username

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError('Invalid email or password')

        data = super().validate(attrs)
        return data

class CommuneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commune
        fields = '__all__'

    def validate(self, data):
        print("Données reçues pour Commune:", data)
        return super().validate(data)

class PhotoMaisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoMaison
        fields = '__all__'

    def validate(self, data):
        print("Données reçues pour PhotoMaison:", data)
        return super().validate(data)

class CommoditeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commodite
        fields = '__all__'

    def validate(self, data):
        print("Données reçues pour Commodite:", data)
        return super().validate(data)

class CommoditeMaisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommoditeMaison
        fields = '__all__'

    def validate(self, data):
        print("Données reçues pour CommoditeMaison:", data)
        return super().validate(data)

class AgenceImmoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgenceImmo
        fields = '__all__'

    def validate(self, data):
        print("Données reçues pour AgenceImmo:", data)
        return super().validate(data)

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

    def validate(self, data):
        print("Données reçues pour Document:", data)
        return super().validate(data)

class MaisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maison
        fields = '__all__'

    def validate(self, data):
        print("Données reçues pour Maison:", data)
        return super().validate(data)

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

    def validate(self, data):
        print("Données reçues pour Location:", data)
        return super().validate(data)

class PaiementLoyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaiementLoyer
        fields = '__all__'

    def validate(self, data):
        print("Données reçues pour PaiementLoyer:", data)
        return super().validate(data)

class PenaliteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Penalite
        fields = '__all__'

    def validate(self, data):
        print("Données reçues pour Penalite:", data)
        return super().validate(data)