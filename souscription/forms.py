from django import forms
from .models import Souscription

class SouscriptionForm(forms.ModelForm):
    documents_fournis = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple': True}), required=False)

    class Meta:
        model = Souscription
        fields = ['locataire', 'maison', 'message_locataire', 'documents_fournis']
        widgets = {
            'locataire': forms.Select(attrs={'class': 'form-select'}),
            'maison': forms.Select(attrs={'class': 'form-select'}),
            'message_locataire': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Votre message à l\'agence'}),
        }