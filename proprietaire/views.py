from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from .models import Proprietaire
from .forms import ProprietaireForm
from agence.models import Agence
from agence.views import role_required, agence_permission  # Utilisation des décorateurs existants

class ProprietairesListView(ListView):
    model = Proprietaire
    template_name = 'proprietaires_list.html'
    context_object_name = 'proprietaires'

    @method_decorator(login_required)
    @method_decorator(role_required(['admin', 'employe']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        # Superuser ou admin voit tous les propriétaires, les employés sont limités à leur agence
        if self.request.user.is_superuser or (self.request.user.role and self.request.user.role == 'admin'):
            return Proprietaire.objects.all()
        else:
            agence = self.request.user.agences.first()
            return Proprietaire.objects.filter(agence=agence) if agence else Proprietaire.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_superuser or (self.request.user.role and self.request.user.role == 'admin'):
            context['agence'] = None  # Pas de restriction d'agence
        else:
            context['agence'] = self.request.user.agences.first()
        return context

@login_required
def proprietaire_profil(request):
    try:
        proprietaire = Proprietaire.objects.get(email=request.user.email)
        return render(request, 'proprietaire/profil.html', {'proprietaire': proprietaire})
    except Proprietaire.DoesNotExist:
        return render(request, 'proprietaire/profil.html', {'error': 'Propriétaire non trouvé'})

@agence_permission(agence_id_param='agence_id')
@role_required(['admin', 'employe'])
def proprietaire_create(request, agence_id=None):
    # Si superuser ou admin, agence_id peut être fourni ou ignoré
    if request.user.is_superuser or (request.user.role and request.user.role == 'admin'):
        agence = get_object_or_404(Agence, id=agence_id) if agence_id else None
    else:
        agence = request.user.agences.first()
        if agence_id and agence_id != agence.id:
            messages.error(request, "Vous n'êtes pas autorisé à créer un propriétaire pour cette agence.")
            return redirect('proprietaire:proprietaires_list')
    
    if not agence and not (request.user.is_superuser or (request.user.role and request.user.role == 'admin')):
        messages.error(request, "Vous n'êtes pas associé à une agence.")
        return redirect('proprietaire:proprietaires_list')

    if request.method == 'POST':
        form = ProprietaireForm(request.POST, request.FILES)
        if form.is_valid():
            proprietaire = form.save(commit=False)
            if agence:
                proprietaire.agence = agence
            proprietaire.save()
            messages.success(request, "Propriétaire ajouté avec succès.")
            return redirect('proprietaire:proprietaires_list')
        else:
            messages.error(request, "Erreur dans le formulaire.")
    else:
        form = ProprietaireForm()
    return render(request, 'proprietaire/proprietaire_create.html', {'form': form, 'agence': agence})

@agence_permission(agence_id_param='agence_id')
@role_required(['admin', 'employe'])
def proprietaire_update(request, proprietaire_id, agence_id=None):
    # Si superuser ou admin, agence_id peut être fourni ou ignoré
    if request.user.is_superuser or (request.user.role and request.user.role == 'admin'):
        proprietaire = get_object_or_404(Proprietaire, id=proprietaire_id)
        agence = get_object_or_404(Agence, id=agence_id) if agence_id else proprietaire.agence
    else:
        agence = request.user.agences.first()
        proprietaire = get_object_or_404(Proprietaire, id=proprietaire_id, agence=agence)
        if agence_id and agence_id != agence.id:
            messages.error(request, "Vous n'êtes pas autorisé à modifier ce propriétaire.")
            return redirect('proprietaire:proprietaires_list')
    
    if not agence and not (request.user.is_superuser or (request.user.role and request.user.role == 'admin')):
        messages.error(request, "Vous n'êtes pas associé à une agence.")
        return redirect('proprietaire:proprietaires_list')

    if request.method == 'POST':
        form = ProprietaireForm(request.POST, request.FILES, instance=proprietaire)
        if form.is_valid():
            form.save()
            messages.success(request, "Propriétaire mis à jour avec succès.")
            return redirect('proprietaire:proprietaires_list')
        else:
            messages.error(request, "Erreur dans le formulaire.")
    else:
        form = ProprietaireForm(instance=proprietaire)
    return render(request, 'proprietaire/proprietaire_update.html', {'form': form, 'agence': agence, 'proprietaire': proprietaire})

@agence_permission(agence_id_param='agence_id')
@role_required(['admin', 'employe'])
def proprietaire_delete(request, proprietaire_id, agence_id=None):
    # Si superuser ou admin, agence_id peut être fourni ou ignoré
    if request.user.is_superuser or (request.user.role and request.user.role == 'admin'):
        proprietaire = get_object_or_404(Proprietaire, id=proprietaire_id)
        agence = get_object_or_404(Agence, id=agence_id) if agence_id else proprietaire.agence
    else:
        agence = request.user.agences.first()
        proprietaire = get_object_or_404(Proprietaire, id=proprietaire_id, agence=agence)
        if agence_id and agence_id != agence.id:
            messages.error(request, "Vous n'êtes pas autorisé à supprimer ce propriétaire.")
            return redirect('proprietaire:proprietaires_list')
    
    if not agence and not (request.user.is_superuser or (request.user.role and request.user.role == 'admin')):
        messages.error(request, "Vous n'êtes pas associé à une agence.")
        return redirect('proprietaire:proprietaires_list')

    if request.method == 'POST':
        proprietaire.delete()
        messages.success(request, "Propriétaire supprimé avec succès.")
        return redirect('proprietaire:proprietaires_list')
    return render(request, 'proprietaire/proprietaire_delete.html', {'proprietaire': proprietaire, 'agence': agence})