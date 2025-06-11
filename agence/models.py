from django.db import models

class Agence(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20)
    siret = models.CharField(max_length=14)
    date_creation = models.DateTimeField(auto_now_add=True)
    logo = models.ImageField(upload_to='agence_logos/', blank=True, null=True)

    def __str__(self):
        return self.nom