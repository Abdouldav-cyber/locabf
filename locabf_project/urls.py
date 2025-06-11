from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import register

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/agence/', include('agence.urls')),
    path('api/proprietaire/', include('proprietaire.urls')),
    path('api/maison/', include('maison.urls')),
    path('api/locataire/', include('locataire.urls')),
    path('api/souscription/', include('souscription.urls')),
    path('api/contrat/', include('contrat.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', register, name='register'),
    path('', HomeView.as_view(), name='home'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/', include('django.contrib.auth.urls')),  # Inclut password_reset
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)