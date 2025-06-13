from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Agence
from maison.models import Maison
from contrat.models import Contrat
from .permissions import agence_required
from django.contrib.auth.models import User

@login_required
@agence_required
def dashboard(request, agence):
    agences = Agence.objects.filter(id=agence.id)  # Restreint à l'agence de l'utilisateur
    maisons_count = Maison.objects.filter(agence=agence).count()
    contrats_count = Contrat.objects.filter(agence=agence, statut='actif').count()
    taux_occupation = (contrats_count / maisons_count * 100) if maisons_count > 0 else 0
    return render(request, 'agence/dashboard.html', {
        'agences': agences,
        'maisons_count': maisons_count,
        'contrats_count': contrats_count,
        'taux_occupation': round(taux_occupation, 2)
    })

class GestionBiensView(LoginRequiredMixin, TemplateView):
    template_name = 'agence/gestion_biens.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agence = self.request.user.agences.first()
        if not agence:
            return HttpResponseForbidden("Vous n'êtes pas associé à une agence.")
        context['maisons'] = Maison.objects.filter(agence=agence)
        return context

class GestionContratsView(LoginRequiredMixin, TemplateView):
    template_name = 'agence/gestion_contrats.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agence = self.request.user.agences.first()
        if not agence:
            return HttpResponseForbidden("Vous n'êtes pas associé à une agence.")
        context['contrats'] = Contrat.objects.filter(agence=agence)
        return context

class RapportsView(LoginRequiredMixin, TemplateView):
    template_name = 'agence/rapports.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agence = self.request.user.agences.first()
        if not agence:
            return HttpResponseForbidden("Vous n'êtes pas associé à une agence.")
        context['maisons_count'] = Maison.objects.filter(agence=agence).count()
        context['contrats_count'] = Contrat.objects.filter(agence=agence, statut='actif').count()
        context['taux_occupation'] = (context['contrats_count'] / context['maisons_count'] * 100) if context['maisons_count'] > 0 else 0
        return context

@login_required
@agence_required
def agence_list(request, agence):
    agences = Agence.objects.filter(id=agence.id)  # Restreint à l'agence de l'utilisateur
    return render(request, 'agence/agence_list.html', {'agences': agences})

@login_required
def agence_create(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        adresse = request.POST['adresse']
        email = request.POST['email']
        telephone = request.POST['telephone']
        siret = request.POST['siret']
        logo = request.FILES.get('logo')

        # Vérification de l'unicité de l'email
        if Agence.objects.filter(email=email).exists():
            messages.error(request, "Cet email est déjà utilisé par une autre agence.")
            return render(request, 'agence/agence_create.html')

        agence = Agence(nom=nom, adresse=adresse, email=email, telephone=telephone, siret=siret, logo=logo)
        agence.save()
        agence.employes.add(request.user)
        messages.success(request, "Agence créée avec succès.")
        return redirect('agence:agence_list')
    return render(request, 'agence/agence_create.html')

@login_required
@agence_required
def agence_update(request, agence_id, agence):
    agence_obj = get_object_or_404(Agence, id=agence_id)
    if agence_obj != agence:
        return HttpResponseForbidden("Vous n'avez pas la permission de modifier cette agence.")
    if request.method == 'POST':
        agence_obj.nom = request.POST['nom']
        agence_obj.adresse = request.POST['adresse']
        agence_obj.email = request.POST['email']
        agence_obj.telephone = request.POST['telephone']
        agence_obj.siret = request.POST['siret']
        if 'logo' in request.FILES:
            agence_obj.logo = request.FILES['logo']
        # Vérification de l'unicité de l'email (sauf si inchangé)
        if agence_obj.email != request.POST['email'] and Agence.objects.filter(email=request.POST['email']).exclude(id=agence_id).exists():
            messages.error(request, "Cet email est déjà utilisé par une autre agence.")
            return render(request, 'agence/agence_update.html', {'agence': agence_obj})
        agence_obj.save()
        messages.success(request, "Agence mise à jour avec succès.")
        return redirect('agence:agence_list')
    return render(request, 'agence/agence_update.html', {'agence': agence_obj})

@login_required
@agence_required
def agence_delete(request, agence_id, agence):
    agence_obj = get_object_or_404(Agence, id=agence_id)
    if agence_obj != agence:
        return HttpResponseForbidden("Vous n'avez pas la permission de supprimer cette agence.")
    if request.method == 'POST':
        agence_obj.delete()
        messages.success(request, "Agence supprimée avec succès.")
        return redirect('home')
    return render(request, 'agence/agence_delete.html', {'agence': agence_obj})

@login_required
@agence_required
def ajouter_employe(request, agence_id, agence):
    agence_obj = get_object_or_404(Agence, id=agence_id)
    if agence_obj != agence:
        return HttpResponseForbidden("Vous n'avez pas la permission d'ajouter un employé à cette agence.")
    if request.method == 'POST':
        email = request.POST.get('email')
        user = get_object_or_404(User, email=email)
        agence_obj.employes.add(user)
        messages.success(request, "Employé ajouté avec succès.")
        return redirect('agence:agence_list')
    return render(request, 'agence/ajouter_employe.html', {'agence': agence_obj})

@login_required
def ajouter_employe_default(request):
    agence = request.user.agences.first()
    if not agence:
        return HttpResponseForbidden("Vous n'êtes pas associé à une agence.")
    return redirect('agence:ajouter_employe', agence_id=agence.id)