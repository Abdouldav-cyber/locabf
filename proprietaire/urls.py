from django.urls import path
from .views import ProprietairesListView, proprietaire_profil
app_name = 'proprietaire'
urlpatterns = [
    path('liste/', ProprietairesListView.as_view(), name='proprietaires_list'),
    path('profil/', proprietaire_profil, name='proprietaire_profil'),
]