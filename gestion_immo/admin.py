from django.contrib import admin
from .models import (
    Commune, PhotoMaison, Commodite, CommoditeMaison,
    AgenceImmo, TypeDocument, Maison, Location,
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
    list_filter = ('sup',)

@admin.register(AgenceImmo)
class AgenceImmoAdmin(admin.ModelAdmin):
    list_display = ('nom', 'immatriculation', 'ville', 'quartier', 'sup')
    search_fields = ('nom', 'immatriculation', 'ville', 'quartier')
    list_filter = ('sup',)

@admin.register(TypeDocument)
class TypeDocumentAdmin(admin.ModelAdmin):
    list_display = ('nom', 'sup')
    search_fields = ('nom',)
    list_filter = ('sup',)

@admin.register(Maison)
class MaisonAdmin(admin.ModelAdmin):
    list_display = ('immat', 'quartier', 'loyer', 'etat', 'commune', 'agence')
    list_filter = ('etat', 'commune', 'agence')
    search_fields = ('immat', 'quartier')

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'client', 'maison', 'date_etablissement', 'date_expiration', 'sup')
    search_fields = ('nom', 'prenom', 'numero')
    list_filter = ('sup', 'date_etablissement')

@admin.register(PaiementLoyer)
class PaiementLoyerAdmin(admin.ModelAdmin):
    list_display = ('date_paiement', 'numero_facture', 'montant', 'location', 'sup')
    search_fields = ('numero_facture',)
    list_filter = ('sup', 'date_paiement')

@admin.register(Penalite)
class PenaliteAdmin(admin.ModelAdmin):
    list_display = ('montant', 'route', 'sup')
    list_filter = ('sup',)
