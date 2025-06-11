from django.contrib import admin
from .models import Locataire

@admin.register(Locataire)
class LocataireAdmin(admin.ModelAdmin):
    list_display = ('nom_complet', 'email', 'telephone', 'profession', 'revenus_mensuels', 'statut_actif')
    search_fields = ('nom_complet', 'email', 'profession')
    list_filter = ('statut_actif', 'date_inscription')
    ordering = ('nom_complet',)
    fieldsets = (
        (None, {
            'fields': ('nom_complet', 'email', 'telephone', 'date_naissance', 'profession', 'revenus_mensuels', 'adresse_actuelle', 'statut_actif')
        }),
    )