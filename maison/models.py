from django.db import models
from proprietaire.models import Proprietaire

class Maison(models.Model):
    STATUT_CHOICES = [
        ('disponible', 'Disponible'),
        ('loue', 'Loué'),
        ('maintenance', 'En maintenance'),
        ('hors_service', 'Hors service'),
    ]
    TYPE_BIEN_CHOICES = [
        ('appartement', 'Appartement'),
        ('maison', 'Maison'),
        ('studio', 'Studio'),
    ]

    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255)
    description = models.TextField()
    adresse_complete = models.TextField()
    ville = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    nombre_pieces = models.IntegerField()
    surface = models.DecimalField(max_digits=10, decimal_places=2)
    type_bien = models.CharField(max_length=50, choices=TYPE_BIEN_CHOICES)
    loyer_mensuel = models.DecimalField(max_digits=10, decimal_places=2)
    charges = models.DecimalField(max_digits=10, decimal_places=2)
    depot_garantie = models.DecimalField(max_digits=10, decimal_places=2)
    meuble = models.BooleanField(default=False)
    statut = models.CharField(max_length=50, choices=STATUT_CHOICES, default='disponible')
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

class Photo(models.Model):
    maison = models.ForeignKey(Maison, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField(upload_to='maison_photos/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Photo de {self.maison.titre}"