from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Contrat
from .serializers import ContratSerializer

class ContratViewSet(viewsets.ModelViewSet):
    queryset = Contrat.objects.all()
    serializer_class = ContratSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

@login_required
def contrat_detail(request, pk):
    contrat = Contrat.objects.get(pk=pk)
    return render(request, 'contrat/contrat_detail.html', {'contrat': contrat})