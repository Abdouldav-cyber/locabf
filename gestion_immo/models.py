from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Commune(models.Model):
    nom = models.CharField(max_length=255)
    sup = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

class Commodite(models.Model):
    nom = models.CharField(max_length=255)
    sup = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

class PhotoMaison(models.Model):
    donnee = models.ImageField(upload_to='photos/')
    libelle = models.CharField(max_length=255, blank=True)
    sup = models.BooleanField(default=False)
    maison = models.ForeignKey('Maison', on_delete=models.CASCADE, related_name='photos')

    def __str__(self):
        return f"Photo de {self.maison.immat}"

class CommoditeMaison(models.Model):
    commodite = models.ForeignKey(Commodite, on_delete=models.CASCADE, related_name='commodite_maisons')
    maison = models.ForeignKey('Maison', on_delete=models.CASCADE, related_name='commodite_maisons')
    nombre = models.IntegerField()
    sup = models.BooleanField(default=False)

class TypeDocument(models.Model):
    nom = models.CharField(max_length=255)
    sup = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

class AgenceImmo(models.Model):
    nom = models.CharField(max_length=255)
    immatriculation = models.CharField(max_length=10, unique=True, null=True, blank=True)
    ville = models.CharField(max_length=255)
    quartier = models.CharField(max_length=255, null=True, blank=True)
    lien_google_maps = models.URLField(blank=True)
    logo = models.ImageField(upload_to='logos/', blank=True)
    sup = models.BooleanField(default=False)

    def __str__(self):
        return self.nom

    def __str__(self):
        return self.nom

class Maison(models.Model):
    OCCUPEE = 'OCCUPEE'
    LIBRE = 'LIBRE'
    ETAT_CHOICES = [
        (OCCUPEE, 'Occupée'),
        (LIBRE, 'Libre')
    ]

    immat = models.CharField(max_length=100, unique=True, null=True, blank=True)
    loyer = models.IntegerField()
    quartier = models.CharField(max_length=255, null=True, blank=True)  # nullable & blankable
    google_maps = models.URLField(blank=True)
    etat = models.CharField(max_length=10, choices=ETAT_CHOICES, default=LIBRE)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name='maisons')
    agence = models.ForeignKey(AgenceImmo, on_delete=models.CASCADE, related_name='maisons')

    def save(self, *args, **kwargs):
        if not self.immat and self.agence:
            prefix = self.agence.immatriculation or "DEF"
            last_maison = Maison.objects.filter(agence=self.agence).order_by('-id').first()
            number = (last_maison.id + 1) if last_maison else 1
            self.immat = f"{prefix}-{number:04d}"
        super().save(*args, **kwargs)
class Location(models.Model):
    date = models.DateField(null=True, blank=True)  # autorise null et vide
    type_document = models.ForeignKey(TypeDocument, on_delete=models.SET_NULL, null=True, blank=True, related_name='locations')  # nullable + blank
    numero = models.CharField(max_length=100, null=True, blank=True)  # autorise null et vide
    date_etablissement = models.DateField(null=True, blank=True)  # autorise null et vide
    date_expiration = models.DateField(null=True, blank=True)  # autorise null et vide
    nom = models.CharField(max_length=100, null=True, blank=True)  # autorise null et vide
    prenom = models.CharField(max_length=100, null=True, blank=True)  # autorise null et vide
    client = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        related_name='gestion_immo_locations',
        null=True,  # autorise null si besoin
        blank=True
    )
    maison = models.ForeignKey(Maison, on_delete=models.CASCADE, related_name='locations', null=True, blank=True)
    cloture = models.BooleanField(default=False)
    sup = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.cloture and self.maison:
            self.maison.etat = Maison.OCCUPEE
            self.maison.save()
        super().save(*args, **kwargs)

@receiver(post_save, sender=Location)
def update_maison_etat_on_cloture(sender, instance, **kwargs):
    if instance.cloture:
        instance.maison.etat = Maison.LIBRE
        instance.maison.save()

class PaiementLoyer(models.Model):
    date_paiement = models.DateTimeField(default=timezone.now)
    numero_facture = models.CharField(max_length=100, blank=True, null=True)  # nullable
    montant = models.IntegerField(null=True, blank=True)  # nullable pour éviter demande défaut
    sup = models.BooleanField(default=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='paiements', null=True, blank=True)  # nullable

    def __str__(self):
        return f"Paiement {self.numero_facture or 'N/A'} - Montant: {self.montant or 'N/A'}"

class Penalite(models.Model):
    montant = models.IntegerField()
    sup = models.BooleanField(default=False)
    route = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='penalites')
