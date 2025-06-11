from django.db import models

class Locataire(models.Model):
    nom_complet = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20)
    date_naissance = models.DateField()
    profession = models.CharField(max_length=100)
    revenus_mensuels = models.DecimalField(max_digits=10, decimal_places=2)
    adresse_actuelle = models.TextField()
    date_inscription = models.DateTimeField(auto_now_add=True)
    statut_actif = models.BooleanField(default=True)

    def __str__(self):
        return self.nom_complet