from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import register, home, access_admin, access_employe, access_proprietaire, access_locataire, login_redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agences/', include('agence.urls', namespace='agence')),
    path('proprietaires/', include('proprietaire.urls', namespace='proprietaire')),
    path('maisons/', include('maison.urls', namespace='maison')),
    path('locataires/', include('locataire.urls', namespace='locataire')),
    path('souscriptions/', include('souscription.urls', namespace='souscription')),
    path('contrats/', include('contrat.urls', namespace='contrat')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html', redirect_authenticated_user=True, next_page='login_redirect'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', register, name='register'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('home/', home, name='home'),
    path('access_admin/', access_admin, name='access_admin'),
    path('access_employe/', access_employe, name='access_employe'),
    path('access_proprietaire/', access_proprietaire, name='access_proprietaire'),
    path('access_locataire/', access_locataire, name='access_locataire'),
    path('login-redirect/', login_redirect, name='login_redirect'),
    path('', lambda request: redirect('home')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Ajout de la gestion des fichiers statiques pour le développement
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)