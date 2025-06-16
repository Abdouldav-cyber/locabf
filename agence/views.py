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

# Décorateur personnalisé pour les permissions d'agence
def agence_permission(agence_id_param=None):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.error(request, "Vous devez être connecté pour accéder à cette page.")
                return redirect('login')
            
            # Si l'utilisateur est superuser ou admin, il a accès à tout sans restriction d'agence
            if request.user.is_superuser or (request.user.role and request.user.role == 'admin'):
                if agence_id_param:
                    agence_id = kwargs.get(agence_id_param)
                    agence = get_object_or_404(Agence, id=agence_id) if agence_id else Agence.objects.first()
                else:
                    agence = None  # Pas de restriction d'agence pour admin/superuser
            else:
                if agence_id_param:
                    agence_id = kwargs.get(agence_id_param)
                    agence = get_object_or_404(Agence, id=agence_id, users=request.user)
                else:
                    agence = request.user.agences.first()
            
            if not agence and not (request.user.is_superuser or (request.user.role and request.user.role == 'admin')):
                messages.error(request, "Vous n'êtes pas associé à une agence ou aucune agence n'est disponible.")
                return redirect('home')
            
            kwargs['agence'] = agence
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator

# Décorateur pour les rôles
def role_required(roles):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated or (request.user.role and request.user.role not in roles and not request.user.is_superuser):
                messages.error(request, "Vous n'avez pas les permissions nécessaires pour accéder à cette page.")
                return redirect('home')
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

# Vue home
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    login_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agence = self.request.user.agences.first()
        if self.request.user.is_superuser or (request.user.role and request.user.role == 'admin'):
            agence = None  # Pas de restriction d'agence pour admin/superuser
        else:
            if not agence:
                agence = Agence.objects.first() if self.request.user.is_superuser else None
        context['agence'] = agence
        return context

@agence_permission()
@role_required(['admin', 'employe'])
def dashboard(request, agence=None):
    if request.user.is_superuser or (request.user.role and request.user.role == 'admin'):
        maisons_count = Maison.objects.count()
        contrats_count = Contrat.objects.filter(statut='actif').count()
    else:
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
        if request.user.is_superuser or (request.user.role and request.user.role == 'admin'):
            context['maisons'] = Maison.objects.all()
            context['agence'] = None
        else:
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
        if request.user.is_superuser or (request.user.role and request.user.role == 'admin'):
            context['contrats'] = Contrat.objects.all()
            context['agence'] = None
        else:
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
        if request.user.is_superuser or (request.user.role and request.user.role == 'admin'):
            context['maisons_count'] = Maison.objects.count()
            context['contrats_count'] = Contrat.objects.filter(statut='actif').count()
        else:
            agence = self.request.user.agences.first()
            if not agence:
                return HttpResponseForbidden("Vous n'êtes pas associé à une agence.")
            context['maisons_count'] = Maison.objects.filter(agence=agence).count()
            context['contrats_count'] = Contrat.objects.filter(agence=agence, statut='actif').count()
        context['taux_occupation'] = (context['contrats_count'] / context['maisons_count'] * 100) if context['maisons_count'] > 0 else 0
        context['agence'] = None if (request.user.is_superuser or (request.user.role and request.user.role == 'admin')) else agence
        return context

@agence_permission()
@role_required(['admin', 'employe'])
def agence_list(request, agence=None):
    if request.user.is_superuser or (request.user.role and request.user.role == 'admin'):
        agences = Agence.objects.all()
    else:
        agences = request.user.agences.all()
    return render(request, 'agence/agence_list.html', {'agences': agences, 'agence': agence})

@agence_permission()
@role_required(['admin'])
def agence_create(request, agence=None):
    if request.method == 'POST':
        form = AgenceForm(request.POST, request.FILES)
        if form.is_valid():
            agence = form.save(commit=False)
            agence.save()
            if not request.user.is_superuser and request.user.role != 'admin':
                agence.users.add(request.user)
            messages.success(request, "Agence créée avec succès.")
            return redirect('agence:agence_list')
        else:
            messages.error(request, "Erreur dans le formulaire.")
    else:
        form = AgenceForm()
    return render(request, 'agence/agence_create.html', {'form': form})

@agence_permission(agence_id_param='agence_id')
@role_required(['admin'])
def agence_update(request, agence_id, agence=None):
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

@agence_permission(agence_id_param='agence_id')
@role_required(['admin'])
def agence_delete(request, agence_id, agence=None):
    if request.method == 'POST':
        agence.delete()
        messages.success(request, "Agence supprimée avec succès.")
        return redirect('agence:agence_list')
    return render(request, 'agence/agence_delete.html', {'agence': agence})

@agence_permission(agence_id_param='agence_id')
@role_required(['admin', 'employe'])
def agence_detail(request, agence_id, agence=None):
    return render(request, 'agence/agence_detail.html', {'agence': agence})

@agence_permission(agence_id_param='agence_id')
@role_required(['admin'])
def ajouter_employe(request, agence_id, agence=None):
    if request.method == 'POST':
        form = EmployeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                if user in agence.users.all():
                    messages.error(request, "Cet employé est déjà associé à l'agence.")
                else:
                    agence.users.add(user)
                    messages.success(request, "Employé ajouté avec succès.")
                    return redirect('agence:agence_list')
            except User.DoesNotExist:
                messages.error(request, "Aucun utilisateur trouvé avec cet email.")
        else:
            messages.error(request, "Erreur dans le formulaire.")
    else:
        form = EmployeForm()
    return render(request, 'agence/ajouter_employe.html', {'form': form, 'agence': agence})

@login_required
def ajouter_employe_default(request):
    if request.user.is_superuser or (request.user.role and request.user.role == 'admin'):
        agence = Agence.objects.first()
    else:
        agence = request.user.agences.first()
    if not agence:
        messages.error(request, "Vous n'êtes pas associé à une agence.")
        return redirect('home')
    return redirect('agence:ajouter_employe', agence_id=agence.id)