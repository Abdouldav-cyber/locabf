from django import forms
from .models import Maison, Photo

class MaisonForm(forms.ModelForm):
    class Meta:
        model = Maison
        fields = [
            'proprietaire', 'titre', 'description', 'adresse_complete', 'ville', 'code_postal',
            'latitude', 'longitude', 'nombre_pieces', 'surface', 'type_bien', 'loyer_mensuel',
            'charges', 'depot_garantie', 'meuble', 'statut'
        ]
        widgets = {
            'proprietaire': forms.Select(attrs={'class': 'form-select'}),
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre du bien'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Description'}),
            'adresse_complete': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse complète'}),
            'ville': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ville'}),
            'code_postal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code postal'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Latitude'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Longitude'}),
            'nombre_pieces': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de pièces'}),
            'surface': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Surface en m²'}),
            'type_bien': forms.Select(attrs={'class': 'form-select'}),
            'loyer_mensuel': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Loyer mensuel (€)'}),
            'charges': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Charges (€)'}),
            'depot_garantie': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Dépôt de garantie (€)'}),
            'meuble': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'statut': forms.Select(attrs={'class': 'form-select'}),
        }

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'description']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description de la photo'}),
        }