from django import forms
from .models import Locataire

class LocataireForm(forms.ModelForm):
    class Meta:
        model = Locataire
        fields = ['nom_complet', 'email', 'telephone', 'date_naissance', 'profession', 'revenus_mensuels', 'adresse_actuelle', 'statut_actif']
        widgets = {
            'nom_complet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom complet'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
            'date_naissance': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'profession': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Profession'}),
            'revenus_mensuels': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Revenus mensuels (€)'}),
            'adresse_actuelle': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Adresse actuelle'}),
            'statut_actif': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        
        }