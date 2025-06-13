from django import forms
from .models import Agence

class AgenceForm(forms.ModelForm):
    class Meta:
        model = Agence
        fields = ['nom', 'adresse', 'email', 'telephone', 'siret', 'logo']

class EmployeForm(forms.Form):
    email = forms.EmailField(label="Email de l'employé", required=True)