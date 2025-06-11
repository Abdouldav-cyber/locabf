from django import forms
from .models import Agence

class AgenceForm(forms.ModelForm):
    class Meta:
        model = Agence
        fields = ['nom', 'adresse', 'email', 'telephone', 'siret', 'logo']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de l\'agence'}),
            'adresse': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Adresse complète'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
            'siret': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numéro SIRET'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
        }