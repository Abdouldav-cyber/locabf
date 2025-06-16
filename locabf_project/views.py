from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from agence.models import User
from .forms import CustomUserCreationForm

def home(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        if role in dict(User.ROLE_CHOICES).keys():
            if request.user.is_authenticated:
                if request.user.role == role:
                    return redirect(f'access_{role}')
                else:
                    messages.error(request, f"Accès réservé au rôle {role}. Votre rôle actuel est {request.user.role}.")
            else:
                # Stocke le rôle choisi dans la session
                request.session['selected_role'] = role
                return redirect('login')
        else:
            messages.error(request, 'Rôle invalide.')
    elif request.user.is_authenticated:
        # Redirige vers la page d'accès du rôle de l'utilisateur connecté
        return redirect(f'access_{request.user.role}')
    return render(request, 'home.html', {'roles': User.ROLE_CHOICES})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Compte créé avec succès ! Veuillez vous connecter.')
            return redirect('login')
        else:
            messages.error(request, 'Erreur dans le formulaire. Vérifiez les champs.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def login_redirect(request):
    # Récupère le rôle sélectionné avant connexion, sinon utilise le rôle de l'utilisateur
    selected_role = request.session.pop('selected_role', None)
    if selected_role and selected_role in dict(User.ROLE_CHOICES).keys() and request.user.role == selected_role:
        return redirect(f'access_{selected_role}')
    return redirect(f'access_{request.user.role}')

@login_required
def access_admin(request):
    if request.user.role != 'admin' and not request.user.is_superuser:
        return HttpResponseForbidden("Accès réservé aux administrateurs.")
    return render(request, 'access_admin.html')

@login_required
def access_employe(request):
    if request.user.role != 'employe':
        return HttpResponseForbidden("Accès réservé aux employés.")
    return render(request, 'access_employe.html')

@login_required
def access_proprietaire(request):
    if request.user.role != 'proprietaire':
        return HttpResponseForbidden("Accès réservé aux propriétaires.")
    return render(request, 'access_proprietaire.html')

@login_required
def access_locataire(request):
    if request.user.role != 'locataire':
        return HttpResponseForbidden("Accès réservé aux locataires.")
    return render(request, 'access_locataire.html')