from django.test import TestCase
from .models import Souscription
from locataire.models import Locataire
from maison.models import Maison
from proprietaire.models import Proprietaire
from datetime import date

class SouscriptionTests(TestCase):
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
            description="Bel appartement",
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
        self.locataire = Locataire.objects.create(
            nom_complet="Marie Martin",
            email="marie.martin@example.com",
            telephone="0123456789",
            date_naissance=date(1990, 5, 10),
            profession="Enseignante",
            revenus_mensuels=2500.00,
            adresse_actuelle="456 Rue Exemple, 75002 Paris"
        )
        self.souscription = Souscription.objects.create(
            locataire=self.locataire,
            maison=self.maison,
            message_locataire="Intéressé par l'appartement",
            statut="en_attente",
            documents_fournis={"files": ["contrat_travail.pdf"]}
        )

    def test_souscription_creation(self):
        self.assertEqual(self.souscription.locataire.nom_complet, "Marie Martin")
        self.assertEqual(self.souscription.maison.titre, "Appartement Paris")
        self.assertEqual(str(self.souscription), f"Souscription {self.souscription.id} - Marie Martin pour Appartement Paris")