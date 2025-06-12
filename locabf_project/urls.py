from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import register, HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agences/', include('agence.urls', namespace='agence')),
    path('proprietaires/', include('proprietaire.urls', namespace='proprietaire')),
    path('maisons/', include('maison.urls', namespace='maison')),
    path('locataires/', include('locataire.urls', namespace='locataire')),
    path('souscriptions/', include('souscription.urls', namespace='souscription')),
    path('contrats/', include('contrat.urls', namespace='contrat')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html', redirect_authenticated_user=True), name='login'),
    path('register/', register, name='register'),
    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)