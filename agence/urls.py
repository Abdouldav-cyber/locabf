from django.urls import path
from . import views

app_name = 'agence'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('list/', views.agence_list, name='agence_list'),
    path('creer/', views.agence_create, name='agence_create'),
    path('modifier/<int:agence_id>/', views.agence_update, name='agence_update'),
    path('supprimer/<int:agence_id>/', views.agence_delete, name='agence_delete'),
    path('ajouter-employe/<int:agence_id>/', views.ajouter_employe, name='ajouter_employe'),
    path('ajouter-employe/', views.ajouter_employe_default, name='ajouter_employe_default'),
    path('details/<int:agence_id>/', views.agence_detail, name='agence_detail'),
    path('gestion-biens/', views.GestionBiensView.as_view(), name='gestion_biens'),
    path('gestion-contrats/', views.GestionContratsView.as_view(), name='gestion_contrats'),
    path('rapports/', views.RapportsView.as_view(), name='rapports'),
]