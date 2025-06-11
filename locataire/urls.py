from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocataireViewSet, recherche_maisons

router = DefaultRouter()
router.register(r'locataires', LocataireViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('recherche/', recherche_maisons, name='recherche_maisons'),
]