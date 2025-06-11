from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MaisonViewSet, maison_list, maison_detail

router = DefaultRouter()
router.register(r'maisons', MaisonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('list/', maison_list, name='maison_list'),
    path('detail/<int:pk>/', maison_detail, name='maison_detail'),
    #path('recherche/', recherche_maisons, name='recherche_maisons'),
]