from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Proprietaire
from .serializers import ProprietaireSerializer

class ProprietaireViewSet(viewsets.ModelViewSet):
    queryset = Proprietaire.objects.all()
    serializer_class = ProprietaireSerializer
    permission_classes = [IsAuthenticated]

@login_required
def proprietaire_profil(request):
    proprietaire = Proprietaire.objects.get(email=request.user.email)
    return render(request, 'proprietaire/profil.html', {'proprietaire': proprietaire})