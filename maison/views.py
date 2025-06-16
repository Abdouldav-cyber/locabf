from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Maison
from .forms import MaisonForm, PhotoForm
from django.urls import reverse

@login_required
def maison_list(request, agence_id=None):
    if agence_id:
        maisons = Maison.objects.filter(agence_id=agence_id)
    else:
        maisons = Maison.objects.all()
    return render(request, 'maison/maison_list.html', {'maisons': maisons, 'agence_id': agence_id})

@login_required
def maison_create(request):
    if request.user.role not in ['admin', 'proprietaire'] or not request.user.is_superuser:
        return HttpResponseForbidden("Accès réservé aux administrateurs ou propriétaires.")
    if request.method == 'POST':
        maison_form = MaisonForm(request.POST)
        photo_form = PhotoForm(request.POST, request.FILES)
        if maison_form.is_valid() and photo_form.is_valid():
            maison = maison_form.save(commit=False)
            maison.proprietaire = request.user if request.user.role == 'proprietaire' else maison_form.cleaned_data['proprietaire']
            maison.agence = request.user.agence if hasattr(request.user, 'agence') else None
            maison.save()
            photo = photo_form.save(commit=False)
            photo.maison = maison
            photo.save()
            messages.success(request, 'Maison créée avec succès !')
            return redirect(reverse('maison:maisons_list'))
        else:
            messages.error(request, 'Erreur dans le formulaire.')
    else:
        maison_form = MaisonForm()
        photo_form = PhotoForm()
    return render(request, 'maison/maison_create.html', {'maison_form': maison_form, 'photo_form': photo_form})

@login_required
def maison_detail(request, pk):
    maison = get_object_or_404(Maison, pk=pk)
    if request.user.role not in ['admin', 'proprietaire'] or maison.proprietaire != request.user:
        return HttpResponseForbidden("Accès refusé.")
    return render(request, 'maison/maison_detail.html', {'maison': maison})

@login_required
def maison_update(request, pk):
    maison = get_object_or_404(Maison, pk=pk)
    if request.user.role not in ['admin', 'proprietaire'] or maison.proprietaire != request.user:
        return HttpResponseForbidden("Accès refusé.")
    if request.method == 'POST':
        maison_form = MaisonForm(request.POST, instance=maison)
        if maison_form.is_valid():
            maison_form.save()
            messages.success(request, 'Maison mise à jour avec succès !')
            return redirect(reverse('maison:maison_detail', args=[pk]))
        else:
            messages.error(request, 'Erreur dans le formulaire.')
    else:
        maison_form = MaisonForm(instance=maison)
    return render(request, 'maison/maison_update.html', {'maison_form': maison_form, 'maison': maison})

@login_required
def maison_delete(request, pk):
    maison = get_object_or_404(Maison, pk=pk)
    if request.user.role not in ['admin', 'proprietaire'] or maison.proprietaire != request.user:
        return HttpResponseForbidden("Accès refusé.")
    if request.method == 'POST':
        maison.delete()
        messages.success(request, 'Maison supprimée avec succès !')
        return redirect(reverse('maison:maisons_list'))
    return render(request, 'maison/maison_delete.html', {'maison': maison})