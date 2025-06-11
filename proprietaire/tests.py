from django.test import TestCase
from .models import Proprietaire
from datetime import date

class ProprietaireTests(TestCase):
    def setUp(self):
        self.proprietaire = Proprietaire.objects.create(
            nom_complet="Jean Dupont",
            email="jean.dupont@example.com",
            telephone="0123456789",
            adresse="123 Rue Exemple, 75001 Paris",
            date_naissance=date(1980, 1, 1),
            statut_actif=True
        )

    def test_proprietaire_creation(self):
        self.assertEqual(self.proprietaire.nom_complet, "Jean Dupont")
        self.assertEqual(self.proprietaire.email, "jean.dupont@example.com")
        self.assertEqual(str(self.proprietaire), "Jean Dupont")

    def test_proprietaire_unique_email(self):
        with self.assertRaises(Exception):
            Proprietaire.objects.create(
                nom_complet="Marie Martin",
                email="jean.dupont@example.com",  # Email déjà utilisé
                telephone="0987654321",
                adresse="456 Rue Exemple, 75002 Paris",
                date_naissance=date(1985, 2, 2),
                statut_actif=True
            )