from django.contrib import admin
from .models import Contrat

@admin.register(Contrat)
class ContratAdmin(admin.ModelAdmin):
    list_display = ('locataire', 'maison', 'proprietaire', 'date_debut', 'date_fin', 'statut')
    search_fields = ('locataire__nom_complet', 'maison__titre', 'proprietaire__nom_complet')
    list_filter = ('statut', 'date_debut')
    ordering = ('date_debut',)
    fieldsets = (
        (None, {
            'fields': ('maison', 'locataire', 'proprietaire', 'souscription', 'date_debut', 'date_fin', 'loyer_mensuel', 'charges_mensuelles', 'depot_garantie', 'statut', 'document_contrat', 'conditions_particulieres')
        }),
    )