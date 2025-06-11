from django.db import models

class Proprietaire(models.Model):
    nom_complet = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20)
    adresse = models.TextField()
    date_naissance = models.DateField()
    piece_identite = models.FileField(upload_to='proprietaire_docs/', blank=True, null=True)
    date_inscription = models.DateTimeField(auto_now_add=True)
    statut_actif = models.BooleanField(default=True)

    def __str__(self):
        return self.nom_complet