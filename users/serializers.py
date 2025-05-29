# users/serializers.py
from rest_framework import serializers
from .models import CustomUser
from gestion_immo.serializers import AgenceImmoSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    agence = AgenceImmoSerializer(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'agence']