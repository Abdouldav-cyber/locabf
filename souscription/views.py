from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Souscription
from .forms import SouscriptionForm
from maison.models import Maison
from locataire.models import Locataire

@login_required
def souscription_form(request, maison_id):
    maison = Maison.objects.get(pk=maison_id)
    locataire = Locataire.objects.get(email=request.user.email)
    if request.method == 'POST':
        form = SouscriptionForm(request.POST, request.FILES)
        if form.is_valid():
            souscription = form.save(commit=False)
            souscription.locataire = locataire
            souscription.maison = maison
            souscription.documents_fournis = {
                'files': [f.name for f in request.FILES.getlist('documents_fournis')]
            } if request.FILES.getlist('documents_fournis') else {}
            souscription.save()
            return redirect('locataire:recherche_maisons')
    else:
        form = SouscriptionForm()
    return render(request, 'souscription/souscription_form.html', {'form': form, 'maison': maison})

class SouscriptionListView(ListView):
    model = Souscription
    template_name = 'souscription/souscription_list.html'
    context_object_name = 'souscriptions'
    paginate_by = 10

    def get_queryset(self):
        return Souscription.objects.all().order_by('-date_demande')

class SouscriptionDetailView(DetailView):
    model = Souscription
    template_name = 'souscription/souscription_detail.html'
    context_object_name = 'souscription'