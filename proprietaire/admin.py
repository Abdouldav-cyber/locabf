from django.contrib import admin
from .models import Proprietaire

@admin.register(Proprietaire)
class ProprietaireAdmin(admin.ModelAdmin):
    list_display = ('nom_complet', 'email', 'telephone', 'date_inscription', 'statut_actif')
    search_fields = ('nom_complet', 'email')
    list_filter = ('statut_actif', 'date_inscription')
    ordering = ('nom_complet',)
    fieldsets = (
        (None, {
            'fields': ('nom_complet', 'email', 'telephone', 'adresse', 'date_naissance', 'piece_identite', 'statut_actif')
        }),
    )