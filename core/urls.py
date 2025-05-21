from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MaisonViewSet, CommuneViewSet, AgenceImmoViewSet, DocumentViewSet,
    LocationViewSet, PaiementLoyerViewSet, PenaliteViewSet, CommoditeViewSet,
    CommoditeMaisonViewSet, PhotoMaisonViewSet
)

router = DefaultRouter()
router.register(r'maisons', MaisonViewSet)
router.register(r'communes', CommuneViewSet)
router.register(r'agences', AgenceImmoViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'paiements', PaiementLoyerViewSet)
router.register(r'penalites', PenaliteViewSet)
router.register(r'commodites', CommoditeViewSet)
router.register(r'commodite-maisons', CommoditeMaisonViewSet)
router.register(r'photos', PhotoMaisonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]