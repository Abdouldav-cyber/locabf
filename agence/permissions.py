from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

def agence_permission(agence_id=None):
      def check_agence(user):
          if not user.is_authenticated:
              return False
          if user.is_superuser:  # Superuser a accès à tout
              return True
          try:
              agence = user.agences.get(id=agence_id) if agence_id else user.agences.first()
              return agence is not None
          except:
              return False
      return user_passes_test(check_agence, login_url='/accounts/login/')

def agence_required(view_func):
      def _wrapped_view(request, *args, **kwargs):
          if not request.user.is_authenticated:
              return HttpResponseForbidden("Vous devez être connecté.")
          agence = request.user.agences.first()
          if not agence:
              return HttpResponseForbidden("Vous n'êtes pas associé à une agence.")
          kwargs['agence'] = agence
          return view_func(request, *args, **kwargs)
      return _wrapped_view