from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Souscription
from .serializers import SouscriptionSerializer
from maison.models import Maison
from locataire.models import Locataire

class SouscriptionViewSet(viewsets.ModelViewSet):
    queryset = Souscription.objects.all()
    serializer_class = SouscriptionSerializer
    permission_classes = [IsAuthenticated]

@login_required
def souscription_form(request, maison_id):
    maison = Maison.objects.get(pk=maison_id)
    locataire = Locataire.objects.get(email=request.user.email)
    if request.method == 'POST':
        souscription = Souscription(
            locataire=locataire,
            maison=maison,
            message_locataire=request.POST.get('message'),
            documents_fournis={'files': [f.name for f in request.FILES.getlist('documents')]}
        )
        souscription.save()
        return redirect('recherche_maisons')
    return render(request, 'locataire/souscription_form.html', {'maison': maison})