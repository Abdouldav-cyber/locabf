from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Locataire
from maison.models import Maison

@login_required
def recherche_maisons(request):
    maisons = Maison.objects.filter(statut='disponible')
    ville = request.GET.get('ville')
    type_bien = request.GET.get('type_bien')
    loyer_max = request.GET.get('loyer_max')
    nombre_pieces = request.GET.get('nombre_pieces')
    meuble = request.GET.get('meuble')

    if ville:
        maisons = maisons.filter(ville__icontains=ville)
    if type_bien:
        maisons = maisons.filter(type_bien=type_bien)
    if loyer_max:
        maisons = maisons.filter(loyer_mensuel__lte=float(loyer_max))
    if nombre_pieces:
        maisons = maisons.filter(nombre_pieces=int(nombre_pieces))
    if meuble:
        maisons = maisons.filter(meuble=meuble == 'true')

    return render(request, 'locataire/recherche_maisons.html', {'maisons': maisons})