# models.py
from django.db import models
from django.utils import timezone

class Commune(models.Model):
    nom = models.CharField(max_length=255)
    sup = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

class PhotoMaison(models.Model):
    donnee = models.ImageField(upload_to='photos/')
    libelle = models.CharField(max_length=255, blank=True)
    sup = models.BooleanField(default=False)
    maison = models.ForeignKey('Maison', on_delete=models.CASCADE, related_name='photos')

class Commodite(models.Model):
    nom = models.CharField(max_length=255)
    sup = models.BooleanField(default=False)

class CommoditeMaison(models.Model):
    commodite = models.ForeignKey(Commodite, on_delete=models.CASCADE, related_name='commodite_maisons')
    maison = models.ForeignKey('Maison', on_delete=models.CASCADE, related_name='commodite_maisons')
    nombre = models.IntegerField()
    sup = models.BooleanField(default=False)

class AgenceImmo(models.Model):
    nom = models.CharField(max_length=255)
    sigle = models.CharField(max_length=100, blank=True)
    telephone = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    numeroCompte = models.CharField(max_length=100, blank=True)
    ifu = models.CharField(max_length=100, blank=True)
    logo = models.ImageField(upload_to='logos/', blank=True)
    sup = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

class Document(models.Model):
    nom = models.CharField(max_length=255)
    sup = models.BooleanField(default=False)

class Maison(models.Model):
    OCCUPEE = 'OCCUPEE'
    LIBRE = 'LIBRE'
    ETAT_CHOICES = [
        (OCCUPEE, 'Occupée'),
        (LIBRE, 'Libre')
    ]
    
    immat = models.CharField(max_length=100, unique=True)
    loyer = models.IntegerField()
    telDemarceur = models.CharField(max_length=20, blank=True)
    quartier = models.CharField(max_length=255)
    section = models.CharField(max_length=100, blank=True)
    lot = models.IntegerField(null=True, blank=True)
    parcelle = models.IntegerField(null=True, blank=True)
    degLat = models.IntegerField()
    minLat = models.IntegerField()
    secLat = models.FloatField()
    emisphere = models.CharField(max_length=1)
    degLong = models.IntegerField()
    minLong = models.IntegerField()
    secLong = models.FloatField()
    fuseau = models.CharField(max_length=1)
    description = models.TextField(blank=True)
    etat = models.CharField(max_length=10, choices=ETAT_CHOICES, default=LIBRE)
    sup = models.BooleanField(default=False)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name='maisons')
    agence = models.ForeignKey(AgenceImmo, on_delete=models.CASCADE, related_name='maisons')

class Location(models.Model):
    dateEntre = models.DateField()
    dateSortie = models.DateField(null=True, blank=True)
    nomClient = models.CharField(max_length=100)
    prenomClient = models.CharField(max_length=100)
    telephoneClient = models.CharField(max_length=20)
    numeroDocument = models.CharField(max_length=100)
    dateEtabli = models.DateField()
    dateExpi = models.DateField()
    sup = models.BooleanField(default=False)
    maison = models.ForeignKey(Maison, on_delete=models.CASCADE, related_name='locations')
    typeDocument = models.ForeignKey(Document, on_delete=models.SET_NULL, null=True, related_name='locations')

class PaiementLoyer(models.Model):
    datePaiement = models.DateTimeField(default=timezone.now)
    numeroFacture = models.CharField(max_length=100, blank=True)
    montant = models.IntegerField()
    sup = models.BooleanField(default=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='paiements')

class Penalite(models.Model):
    montant = models.IntegerField()
    sup = models.BooleanField(default=False)
    route = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='penalites')
