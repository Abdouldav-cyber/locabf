from django.urls import path
from .views import recherche_maisons

app_name = 'locataire'

urlpatterns = [
    path('recherche/', recherche_maisons, name='recherche_maisons'),
]