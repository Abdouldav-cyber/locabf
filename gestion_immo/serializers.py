# gestion_immo/serializers.py
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from .models import (
    Maison, Commune, AgenceImmo, TypeDocument, Location,
    PaiementLoyer, Penalite, Commodite, CommoditeMaison, PhotoMaison
)

# Import de CustomUserSerializer retiré du top-level pour éviter import circulaire


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'] = serializers.EmailField(required=True)
        self.fields.pop('username', None)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError('Invalid email or password')

        data = super().validate(attrs)

        # Import local pour éviter boucle circulaire
        from users.serializers import CustomUserSerializer
        data['user'] = CustomUserSerializer(user).data

        return data


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
    commodite = CommoditeSerializer(read_only=True)

    class Meta:
        model = CommoditeMaison
        fields = '__all__'


class AgenceImmoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgenceImmo
        fields = '__all__'


class TypeDocumentSerializer(serializers.ModelSerializer):  # Anciennement DocumentSerializer
    class Meta:
        model = TypeDocument
        fields = '__all__'


class MaisonSerializer(serializers.ModelSerializer):
    commune = CommuneSerializer(read_only=True)
    agence = AgenceImmoSerializer(read_only=True)
    photos = PhotoMaisonSerializer(many=True, read_only=True)
    commodite_maisons = CommoditeMaisonSerializer(many=True, read_only=True)

    class Meta:
        model = Maison
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    type_document = TypeDocumentSerializer(read_only=True)
    maison = MaisonSerializer(read_only=True)

    # On ne déclare pas directement CustomUserSerializer ici pour éviter l'import circulaire

    class Meta:
        model = Location
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # Import local pour éviter boucle circulaire
        from users.serializers import CustomUserSerializer

        # Sérialiser 'client' avec CustomUserSerializer si présent
        if instance.client:
            representation['client'] = CustomUserSerializer(instance.client).data
        else:
            representation['client'] = None

        return representation


class PaiementLoyerSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)

    class Meta:
        model = PaiementLoyer
        fields = '__all__'


class PenaliteSerializer(serializers.ModelSerializer):
    route = LocationSerializer(read_only=True)

    class Meta:
        model = Penalite
        fields = '__all__'
