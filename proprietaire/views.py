from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Proprietaire

class ProprietairesListView(ListView):
    model = Proprietaire
    template_name = 'proprietaires_list.html'
    context_object_name = 'proprietaires'

@login_required
def proprietaire_profil(request):
    try:
        proprietaire = Proprietaire.objects.get(email=request.user.email)
        return render(request, 'proprietaire/profil.html', {'proprietaire': proprietaire})
    except Proprietaire.DoesNotExist:
        return render(request, 'proprietaire/profil.html', {'error': 'Propriétaire non trouvé'})