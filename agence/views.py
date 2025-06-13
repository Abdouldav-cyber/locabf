from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseForbidden
from .models import Agence
from maison.models import Maison
from contrat.models import Contrat
from .forms import AgenceForm, EmployeForm
from django.contrib.auth.models import User

# Permissions
def agence_permission(agence_id=None):
    def decorator(view_func):
        @login_required
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponseForbidden("Vous devez être connecté.")
            if request.user.is_superuser:
                kwargs['agence'] = Agence.objects.first()  # Superuser gets first agency or None
                return view_func(request, *args, **kwargs)
            try:
                if agence_id and isinstance(agence_id, str):
                    agence = get_object_or_404(Agence, id=kwargs.get(agence_id), employes=request.user)
                else:
                    agence = request.user.agences.first()
                if not agence:
                    return HttpResponseForbidden("Vous n'êtes pas associé à une agence.")
                kwargs['agence'] = agence
                return view_func(request, *args, **kwargs)
            except Agence.DoesNotExist:
                return HttpResponseForbidden("Vous n'êtes pas associé à cette agence.")
        return wrapper
    return decorator

def agence_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden("Vous devez être connecté.")
        agence_id = kwargs.get('agence_id')
        if agence_id:
            agence = get_object_or_404(Agence, id=agence_id, employes=request.user)
        else:
            agence = request.user.agences.first()
        if not agence:
            return HttpResponseForbidden("Vous n'êtes pas associé à une agence.")
        kwargs['agence'] = agence
        return view_func(request, *args, **kwargs)
    return _wrapped_view

# Views
@agence_permission()
def dashboard(request, agence=None):
    maisons_count = Maison.objects.filter(agence=agence).count()
    contrats_count = Contrat.objects.filter(agence=agence, statut='actif').count()
    taux_occupation = (contrats_count / maisons_count * 100) if maisons_count > 0 else 0
    return render(request, 'agence/dashboard.html', {
        'agence': agence,
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
        context['agence'] = agence
        return context

class GestionContratsView(LoginRequiredMixin, TemplateView):
    template_name = 'agence/gestion_contrats.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agence = self.request.user.agences.first()
        if not agence:
            return HttpResponseForbidden("Vous n'êtes pas associé à une agence.")
        context['contrats'] = Contrat.objects.filter(agence=agence)
        context['agence'] = agence
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
        context['agence'] = agence
        return context

@agence_permission()
def agence_list(request, agence=None):
    if request.user.is_superuser:
        agences = Agence.objects.all()  # Superusers see all agencies
    else:
        agences = request.user.agences.all()  # Regular users see their agencies
    return render(request, 'agence/agence_list.html', {'agences': agences, 'agence': agence})

@agence_permission()
def agence_create(request, agence=None):
    if request.method == 'POST':
        form = AgenceForm(request.POST, request.FILES)
        if form.is_valid():
            agence = form.save(commit=False)
            agence.employes.add(request.user)
            agence.save()
            messages.success(request, "Agence créée avec succès.")
            return redirect('agence:agence_list')
        else:
            messages.error(request, "Erreur dans le formulaire.")
    else:
        form = AgenceForm()
    return render(request, 'agence/agence_create.html', {'form': form})

@agence_permission(agence_id='agence_id')
def agence_update(request, agence_id, agence=None):
    if not agence:
        agence = get_object_or_404(Agence, id=agence_id, employes=request.user)
    if request.method == 'POST':
        form = AgenceForm(request.POST, request.FILES, instance=agence)
        if form.is_valid():
            form.save()
            messages.success(request, "Agence mise à jour avec succès.")
            return redirect('agence:agence_list')
        else:
            messages.error(request, "Erreur dans le formulaire.")
    else:
        form = AgenceForm(instance=agence)
    return render(request, 'agence/agence_update.html', {'form': form, 'agence': agence})

@agence_permission(agence_id='agence_id')
def agence_delete(request, agence_id, agence=None):
    if not agence:
        agence = get_object_or_404(Agence, id=agence_id, employes=request.user)
    if request.method == 'POST':
        agence.delete()
        messages.success(request, "Agence supprimée avec succès.")
        return redirect('agence:agence_list')
    return render(request, 'agence/agence_delete.html', {'agence': agence})

@agence_permission(agence_id='agence_id')
def agence_detail(request, agence_id, agence=None):
    if not agence:
        agence = get_object_or_404(Agence, id=agence_id, employes=request.user)
    return render(request, 'agence/agence_detail.html', {'agence': agence})

@agence_permission(agence_id='agence_id')
def ajouter_employe(request, agence_id, agence=None):
    if not agence:
        agence = get_object_or_404(Agence, id=agence_id, employes=request.user)
    if request.method == 'POST':
        form = EmployeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = get_object_or_404(User, email=email)
            agence.employes.add(user)
            messages.success(request, "Employé ajouté avec succès.")
            return redirect('agence:agence_list')
        else:
            messages.error(request, "Erreur dans le formulaire.")
    else:
        form = EmployeForm()
    return render(request, 'agence/ajouter_employe.html', {'form': form, 'agence': agence})

@login_required
def ajouter_employe_default(request):
    agence = request.user.agences.first()
    if not agence:
        return HttpResponseForbidden("Vous n'êtes pas associé à une agence.")
    return redirect('agence:ajouter_employe', agence_id=agence.id)