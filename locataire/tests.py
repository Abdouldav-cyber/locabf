from django.test import TestCase
from .models import Locataire
from datetime import date

class LocataireTests(TestCase):
    def setUp(self):
        self.locataire = Locataire.objects.create(
            nom_complet="Marie Martin",
            email="marie.martin@example.com",
            telephone="0123456789",
            date_naissance=date(1990, 5, 10),
            profession="Enseignante",
            revenus_mensuels=2500.00,
            adresse_actuelle="456 Rue Exemple, 75002 Paris",
            statut_actif=True
        )

    def test_locataire_creation(self):
        self.assertEqual(self.locataire.nom_complet, "Marie Martin")
        self.assertEqual(self.locataire.email, "marie.martin@example.com")
        self.assertEqual(str(self.locataire), "Marie Martin")

    def test_locataire_unique_email(self):
        with self.assertRaises(Exception):
            Locataire.objects.create(
                nom_complet="Paul Durand",
                email="marie.martin@example.com",  # Email déjà utilisé
                telephone="0987654321",
                date_naissance=date(1988, 3, 15),
                profession="Ingénieur",
                revenus_mensuels=3000.00,
                adresse_actuelle="789 Rue Test, 75003 Paris",
                statut_actif=True
            )