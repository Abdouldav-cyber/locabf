# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'communes', CommuneViewSet)
router.register(r'photos', PhotoMaisonViewSet)
router.register(r'commodites', CommoditeViewSet)
router.register(r'commodite-maisons', CommoditeMaisonViewSet)
router.register(r'agences', AgenceImmoViewSet)
router.register(r'maisons', MaisonViewSet)
router.register(r'documents', DocumentViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'paiements', PaiementLoyerViewSet)
router.register(r'penalites', PenaliteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
