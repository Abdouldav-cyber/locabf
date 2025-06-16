from django import forms
from django.contrib.auth.forms import UserCreationForm
from agence.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Adresse email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Entrez votre email'})
    )
    role = forms.ChoiceField(
        choices=User.ROLE_CHOICES,
        required=True,
        label="Rôle",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Appliquer des attributs supplémentaires aux champs hérités
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Choisissez un nom d\'utilisateur'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Entrez un mot de passe'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirmez le mot de passe'
        })

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Cet email est déjà utilisé.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.role = self.cleaned_data['role']
        if commit:
            user.save()
        return user