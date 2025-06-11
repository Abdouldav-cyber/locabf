from django.test import TestCase
from .models import Maison, Photo
from proprietaire.models import Proprietaire
from datetime import date

class MaisonTests(TestCase):
    def setUp(self):
        self.proprietaire = Proprietaire.objects.create(
            nom_complet="Jean Dupont",
            email="jean.dupont@example.com",
            telephone="0123456789",
            adresse="123 Rue Exemple, 75001 Paris",
            date_naissance=date(1980, 1, 1)
        )
        self.maison = Maison.objects.create(
            proprietaire=self.proprietaire,
            titre="Appartement Paris",
            description="Bel appartement au centre",
            adresse_complete="123 Rue Test, 75001 Paris",
            ville="Paris",
            code_postal="75001",
            latitude=48.8566,
            longitude=2.3522,
            nombre_pieces=3,
            surface=75.5,
            type_bien="appartement",
            loyer_mensuel=1200.00,
            charges=150.00,
            depot_garantie=2400.00,
            meuble=True,
            statut="disponible"
        )

    def test_maison_creation(self):
        self.assertEqual(self.maison.titre, "Appartement Paris")
        self.assertEqual(self.maison.proprietaire.nom_complet, "Jean Dupont")
        self.assertEqual(str(self.maison), "Appartement Paris")

    def test_photo_creation(self):
        photo = Photo.objects.create(
            maison=self.maison,
            image="maison_photos/test.jpg",
            description="Salon"
        )
        self.assertEqual(str(photo), "Photo de Appartement Paris")