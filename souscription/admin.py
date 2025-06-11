from django.contrib import admin
from .models import Souscription

@admin.register(Souscription)
class SouscriptionAdmin(admin.ModelAdmin):
    list_display = ('locataire', 'maison', 'statut', 'date_demande', 'date_reponse')
    search_fields = ('locataire__nom_complet', 'maison__titre')
    list_filter = ('statut', 'date_demande')
    ordering = ('date_demande',)
    fieldsets = (
        (None, {
            'fields': ('locataire', 'maison', 'message_locataire', 'statut', 'date_reponse', 'commentaire_agence', 'documents_fournis')
        }),
    )