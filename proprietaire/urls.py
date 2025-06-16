from django.urls import path
from .views import ProprietairesListView, proprietaire_profil, proprietaire_create, proprietaire_update, proprietaire_delete

app_name = 'proprietaire'
urlpatterns = [
    path('liste/', ProprietairesListView.as_view(), name='proprietaires_list'),
    path('profil/', proprietaire_profil, name='proprietaire_profil'),
    path('creer/<int:agence_id>/', proprietaire_create, name='proprietaire_create'),
    path('modifier/<int:proprietaire_id>/<int:agence_id>/', proprietaire_update, name='proprietaire_update'),
    path('supprimer/<int:proprietaire_id>/<int:agence_id>/', proprietaire_delete, name='proprietaire_delete'),
    # Ajout d'une route sans agence_id pour superuser/admin (optionnel)
    path('creer/', proprietaire_create, name='proprietaire_create_global'),
]