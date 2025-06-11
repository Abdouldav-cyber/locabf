from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProprietaireViewSet, proprietaire_profil

router = DefaultRouter()
router.register(r'proprietaires', ProprietaireViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('profil/', proprietaire_profil, name='proprietaire_profil'),
]