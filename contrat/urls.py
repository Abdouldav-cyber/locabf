from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContratViewSet, contrat_detail

router = DefaultRouter()
router.register(r'contrats', ContratViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('detail/<int:pk>/', contrat_detail, name='contrat_detail'),
]