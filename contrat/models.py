from django.db import models
from maison.models import Maison
from locataire.models import Locataire
from proprietaire.models import Proprietaire
from souscription.models import Souscription

class Contrat(models.Model):
    STATUT_CHOICES = [
        ('actif', 'Actif'),
        ('resilie', 'Résilié'),
        ('termine', 'Terminé'),
        ('suspendu', 'Suspendu'),
    ]

    maison = models.ForeignKey(Maison, on_delete=models.CASCADE)
    locataire = models.ForeignKey(Locataire, on_delete=models.CASCADE)
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    souscription = models.ForeignKey(Souscription, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    loyer_mensuel = models.DecimalField(max_digits=10, decimal_places=2)
    charges_mensuelles = models.DecimalField(max_digits=10, decimal_places=2)
    depot_garantie = models.DecimalField(max_digits=10, decimal_places=2)
    statut = models.CharField(max_length=50, choices=STATUT_CHOICES, default='actif')
    date_signature = models.DateTimeField(auto_now_add=True)
    document_contrat = models.FileField(upload_to='contrats/', blank=True, null=True)
    conditions_particulieres = models.TextField(blank=True)

    def __str__(self):
        return f"Contrat {self.id} - {self.locataire} pour {self.maison}"