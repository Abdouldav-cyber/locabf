from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Agence
from .serializers import AgenceSerializer
from maison.models import Maison
from contrat.models import Contrat

class AgenceViewSet(viewsets.ModelViewSet):
    queryset = Agence.objects.all()
    serializer_class = AgenceSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

@login_required
def dashboard(request):
    agences = Agence.objects.all()
    maisons_count = Maison.objects.count()
    contrats_count = Contrat.objects.filter(statut='actif').count()
    taux_occupation = (contrats_count / maisons_count * 100) if maisons_count > 0 else 0
    return render(request, 'agence/dashboard.html', {
        'agences': agences,
        'maisons_count': maisons_count,
        'contrats_count': contrats_count,
        'taux_occupation': round(taux_occupation, 2)
    })