from django.db import models
from locataire.models import Locataire
from maison.models import Maison

class Souscription(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('acceptee', 'Acceptée'),
        ('refusee', 'Refusée'),
        ('annulee', 'Annulée'),
    ]

    locataire = models.ForeignKey(Locataire, on_delete=models.CASCADE)
    maison = models.ForeignKey(Maison, on_delete=models.CASCADE)
    date_demande = models.DateTimeField(auto_now_add=True)
    message_locataire = models.TextField(blank=True)
    statut = models.CharField(max_length=50, choices=STATUT_CHOICES, default='en_attente')
    date_reponse = models.DateTimeField(blank=True, null=True)
    commentaire_agence = models.TextField(blank=True)
    documents_fournis = models.JSONField(default=dict)

    def __str__(self):
        return f"Souscription {self.id} - {self.locataire} pour {self.maison}"