from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Maison

@login_required
def maison_list(request):
    maisons = Maison.objects.filter(statut='disponible')
    return render(request, 'maison/maison_list.html', {'maisons': maisons})

@login_required
def maison_detail(request, pk):
    maison = Maison.objects.get(pk=pk)
    return render(request, 'maison/maison_detail.html', {'maison': maison})