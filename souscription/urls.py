from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SouscriptionViewSet, souscription_form

router = DefaultRouter()
router.register(r'souscriptions', SouscriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('form/<int:maison_id>/', souscription_form, name='souscription_form'),
]