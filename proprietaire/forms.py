from django import forms
from .models import Proprietaire

class ProprietaireForm(forms.ModelForm):
    class Meta:
        model = Proprietaire
        fields = ['nom_complet', 'email', 'telephone', 'adresse', 'date_naissance', 'piece_identite', 'statut_actif']
        widgets = {
            'nom_complet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom complet'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
            'adresse': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Adresse'}),
            'date_naissance': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'piece_identite': forms.FileInput(attrs={'class': 'form-control'}),
            'statut_actif': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }