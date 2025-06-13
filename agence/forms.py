# agence_app/forms.py (ou votre_app/forms.py)

from django import forms
from .models import Agence

class AgenceForm(forms.ModelForm):
    class Meta:
        model = Agence
        fields = ['nom', 'adresse', 'email', 'telephone', 'siret', 'logo', 'employes']
        # Si vous ne voulez pas inclure 'employes' ou 'logo' dans le formulaire
        # fields = ['nom', 'adresse', 'email', 'telephone', 'siret']v