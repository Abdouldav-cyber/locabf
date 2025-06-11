from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgenceViewSet, dashboard

router = DefaultRouter()
router.register(r'agences', AgenceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('dashboard/', dashboard, name='dashboard'),
]