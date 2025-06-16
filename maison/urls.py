from django.urls import path
from .views import maison_list, maison_detail, maison_create, maison_update, maison_delete

app_name = 'maison'

urlpatterns = [
    path('liste/<int:agence_id>/', maison_list, name='maisons_list'),
    path('liste/all/', maison_list, name='maisons_list_all'),  # Nouvelle URL pour toutes les maisons
    path('detail/<int:pk>/', maison_detail, name='maison_detail'),
    path('creer/', maison_create, name='maison_create'),
    path('modifier/<int:pk>/', maison_update, name='maison_update'),
    path('supprimer/<int:pk>/', maison_delete, name='maison_delete'),
]