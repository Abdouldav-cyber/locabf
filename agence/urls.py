from django.urls import path
from . import views

app_name = 'agence'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('gestion-biens/', views.GestionBiensView.as_view(), name='gestion_biens'),
    path('gestion-contrats/', views.GestionContratsView.as_view(), name='gestion_contrats'),
    path('rapports/', views.RapportsView.as_view(), name='rapports'),
]