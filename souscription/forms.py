from django import forms
from .models import Souscription

class SouscriptionForm(forms.ModelForm):
    documents_fournis = forms.FileField(
        widget=forms.FileInput(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = Souscription
        fields = ['message_locataire', 'documents_fournis']
        widgets = {
            'message_locataire': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Votre message à l\'agence'
            }),
        }