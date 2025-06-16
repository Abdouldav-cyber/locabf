from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from .models import Proprietaire
from .forms import ProprietaireForm
from agence.models import Agence
from agence.views import role_required  # Importe le décorateur personnalisé

class ProprietairesListView(ListView):
    model = Proprietaire
    template_name = 'proprietaires_list.html'
    context_object_name = 'proprietaires'

    @method_decorator(login_required)
    @method_decorator(role_required(['admin', 'employe']))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['agence'] = self.request.user.agences.first()
        return context

@login_required
def proprietaire_profil(request):
    try:
        proprietaire = Proprietaire.objects.get(email=request.user.email)
        return render(request, 'proprietaire/profil.html', {'proprietaire': proprietaire})
    except Proprietaire.DoesNotExist:
        return render(request, 'proprietaire/profil.html', {'error': 'Propriétaire non trouvé'})

@login_required
@role_required(['admin', 'employe'])
def proprietaire_create(request, agence_id=None):
    agence = request.user.agences.first() if not agence_id else get_object_or_404(Agence, id=agence_id)
    if request.method == 'POST':
        form = ProprietaireForm(request.POST, request.FILES)
        if form.is_valid():
            proprietaire = form.save()
            messages.success(request, "Propriétaire ajouté avec succès.")
            return redirect('proprietaire:proprietaires_list')
        else:
            messages.error(request, "Erreur dans le formulaire.")
    else:
        form = ProprietaireForm()
    return render(request, 'proprietaire/proprietaire_create.html', {'form': form, 'agence': agence})

@login_required
@role_required(['admin', 'employe'])
def proprietaire_update(request, proprietaire_id, agence_id=None):
    agence = request.user.agences.first() if not agence_id else get_object_or_404(Agence, id=agence_id)
    proprietaire = get_object_or_404(Proprietaire, id=proprietaire_id)
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

@login_required
@role_required(['admin', 'employe'])
def proprietaire_delete(request, proprietaire_id, agence_id=None):
    agence = request.user.agences.first() if not agence_id else get_object_or_404(Agence, id=agence_id)
    proprietaire = get_object_or_404(Proprietaire, id=proprietaire_id)
    if request.method == 'POST':
        proprietaire.delete()
        messages.success(request, "Propriétaire supprimé avec succès.")
        return redirect('proprietaire:proprietaires_list')
    return render(request, 'proprietaire/proprietaire_delete.html', {'proprietaire': proprietaire, 'agence': agence})