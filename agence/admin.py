from django.contrib import admin
from .models import Agence

@admin.register(Agence)
class AgenceAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'telephone', 'siret', 'date_creation')
    search_fields = ('nom', 'email', 'siret')
    list_filter = ('date_creation',)
    ordering = ('nom',)
    fieldsets = (
        (None, {
            'fields': ('nom', 'adresse', 'email', 'telephone', 'siret', 'logo')
        }),
    )