from django.contrib import admin
from .models import (
    Commune, PhotoMaison, Commodite, CommoditeMaison,
    AgenceImmo, Document, Maison, Location,
    PaiementLoyer, Penalite
)

@admin.register(Commune)
class CommuneAdmin(admin.ModelAdmin):
    list_display = ('nom', 'sup')
    search_fields = ('nom',)

@admin.register(PhotoMaison)
class PhotoMaisonAdmin(admin.ModelAdmin):
    list_display = ('libelle', 'maison', 'sup')
    search_fields = ('libelle',)
    list_filter = ('sup',)

@admin.register(Commodite)
class CommoditeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'sup')
    search_fields = ('nom',)

@admin.register(CommoditeMaison)
class CommoditeMaisonAdmin(admin.ModelAdmin):
    list_display = ('commodite', 'maison', 'nombre', 'sup')

@admin.register(AgenceImmo)
class AgenceImmoAdmin(admin.ModelAdmin):
    list_display = ('nom', 'sigle', 'telephone', 'email', 'sup')
    search_fields = ('nom', 'sigle', 'email')

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('nom', 'sup')

@admin.register(Maison)
class MaisonAdmin(admin.ModelAdmin):
    list_display = ('immat', 'quartier', 'loyer', 'etat', 'commune', 'agence', 'sup')
    list_filter = ('etat', 'commune', 'agence', 'sup')
    search_fields = ('immat', 'quartier', 'description')

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('nomClient', 'prenomClient', 'telephoneClient', 'maison', 'dateEntre', 'dateSortie', 'sup')
    search_fields = ('nomClient', 'prenomClient', 'numeroDocument')
    list_filter = ('sup', 'dateEntre')

@admin.register(PaiementLoyer)
class PaiementLoyerAdmin(admin.ModelAdmin):
    list_display = ('datePaiement', 'numeroFacture', 'montant', 'location', 'sup')
    search_fields = ('numeroFacture',)
    list_filter = ('sup', 'datePaiement')

@admin.register(Penalite)
class PenaliteAdmin(admin.ModelAdmin):
    list_display = ('montant', 'route', 'sup')
    list_filter = ('sup',)
