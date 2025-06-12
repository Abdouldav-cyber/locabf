from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Agence
from maison.models import Maison
from contrat.models import Contrat

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

class GestionBiensView(LoginRequiredMixin, TemplateView):
    template_name = 'agence/gestion_biens.html'

class GestionContratsView(LoginRequiredMixin, TemplateView):
    template_name = 'agence/gestion_contrats.html'

class RapportsView(LoginRequiredMixin, TemplateView):
    template_name = 'agence/rapports.html'