from django.contrib import admin
from .models import Maison, Photo

class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1

@admin.register(Maison)
class MaisonAdmin(admin.ModelAdmin):
    list_display = ('titre', 'proprietaire', 'ville', 'type_bien', 'loyer_mensuel', 'statut')
    search_fields = ('titre', 'ville', 'adresse_complete')
    list_filter = ('type_bien', 'statut', 'meuble')
    ordering = ('titre',)
    inlines = [PhotoInline]
    fieldsets = (
        (None, {
            'fields': ('proprietaire', 'titre', 'description', 'adresse_complete', 'ville', 'code_postal', 'latitude', 'longitude')
        }),
        ('Caractéristiques', {
            'fields': ('nombre_pieces', 'surface', 'type_bien', 'loyer_mensuel', 'charges', 'depot_garantie', 'meuble', 'statut')
        }),
    )

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('maison', 'description')
    search_fields = ('maison__titre', 'description')