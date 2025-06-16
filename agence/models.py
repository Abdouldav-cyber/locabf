from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    agences = models.ManyToManyField('Agence', related_name='users', blank=True)
    ROLE_CHOICES = (
        ('admin', 'Administrateur'),
        ('employe', 'Employé'),
        ('proprietaire', 'Propriétaire'),
        ('locataire', 'Locataire'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='locataire')

    def __str__(self):
        return self.username

class Agence(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20)
    siret = models.CharField(max_length=20)
    date_creation = models.DateTimeField(auto_now_add=True)
    logo = models.ImageField(upload_to='agence_logos/', null=True, blank=True)
    employes = models.ManyToManyField(User, related_name='agence_employes', blank=True)

    def __str__(self):
        return self.nom