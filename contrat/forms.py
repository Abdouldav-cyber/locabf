from django import forms
from .models import Contrat

class ContratForm(forms.ModelForm):
    class Meta:
        model = Contrat
        fields = [
            'maison', 'locataire', 'proprietaire', 'souscription', 'date_debut', 'date_fin',
            'loyer_mensuel', 'charges_mensuelles', 'depot_garantie', 'statut', 'document_contrat',
            'conditions_particulieres'
        ]
        widgets = {
            'maison': forms.Select(attrs={'class': 'form-select'}),
            'locataire': forms.Select(attrs={'class': 'form-select'}),
            'proprietaire': forms.Select(attrs={'class': 'form-select'}),
            'souscription': forms.Select(attrs={'class': 'form-select'}),
            'date_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'loyer_mensuel': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Loyer mensuel (€)'}),
            'charges_mensuelles': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Charges mensuelles (€)'}),
            'depot_garantie': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Dépôt de garantie (€)'}),
            'statut': forms.Select(attrs={'class': 'form-select'}),
            'document_contrat': forms.FileInput(attrs={'class': 'form-control'}),
            'conditions_particulieres': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Conditions particulières'}),
        }