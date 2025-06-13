from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from .models import Agence

def agence_permission(agence_id=None):
    def check_agence(user):
        if not user.is_authenticated:  # Vérifie l'authentification de l'utilisateur
            return False
        if user.is_superuser:  # Superuser a accès à tout
            return True
        try:
            agence = user.agences.get(id=agence_id) if agence_id else user.agences.first()
            return agence is not None
        except Agence.DoesNotExist:
            return False
    return login_required(user_passes_test(check_agence, login_url='/accounts/login/'))

def agence_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:  # Vérifie l'authentification ici
            return HttpResponseForbidden("Vous devez être connecté.")
        agence_id = kwargs.get('agence_id')  # Récupère agence_id depuis les kwargs
        if agence_id:
            agence = get_object_or_404(Agence, id=agence_id, employes=request.user)
        else:
            agence = request.user.agences.first()
        if not agence:
            return HttpResponseForbidden("Vous n'êtes pas associé à une agence.")
        kwargs['agence'] = agence
        return view_func(request, *args, **kwargs)
    return _wrapped_view