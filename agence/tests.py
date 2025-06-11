from django.test import TestCase
from .models import Agence

class AgenceTests(TestCase):
    def setUp(self):
        self.agence = Agence.objects.create(
            nom="Agence Test",
            adresse="123 Rue Test, 75001 Paris",
            email="test@agence.com",
            telephone="0123456789",
            siret="12345678901234"
        )

    def test_agence_creation(self):
        self.assertEqual(self.agence.nom, "Agence Test")
        self.assertEqual(self.agence.email, "test@agence.com")
        self.assertEqual(str(self.agence), "Agence Test")

    def test_agence_unique_email(self):
        with self.assertRaises(Exception):
            Agence.objects.create(
                nom="Agence Test 2",
                adresse="456 Rue Test, 75002 Paris",
                email="test@agence.com",  # Email déjà utilisé
                telephone="0987654321",
                siret="98765432109876"
            )