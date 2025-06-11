from django.test import TestCase
from .models import Contrat
from maison.models import Maison
from locataire.models import Locataire
from proprietaire.models import Proprietaire
from souscription.models import Souscription
from datetime import date

class ContratTests(TestCase):
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
            statut="acceptee"
        )
        self.contrat = Contrat.objects.create(
            maison=self.maison,
            locataire=self.locataire,
            proprietaire=self.proprietaire,
            souscription=self.souscription,
            date_debut=date(2025, 1, 1),
            date_fin=date(2026, 1, 1),
            loyer_mensuel=1200.00,
            charges_mensuelles=150.00,
            depot_garantie=2400.00,
            statut="actif"
        )

    def test_contrat_creation(self):
        self.assertEqual(self.contrat.locataire.nom_complet, "Marie Martin")
        self.assertEqual(self.contrat.maison.titre, "Appartement Paris")
        self.assertEqual(str(self.contrat), f"Contrat {self.contrat.id} - Marie Martin pour Appartement Paris")