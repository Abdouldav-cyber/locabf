"""
Paramètres Django pour le projet gestion_immo.

Généré par 'django-admin startproject' avec Django 5.2.1.
"""

from pathlib import Path
from datetime import timedelta

# Chemin de base du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# Clé secrète (à sécuriser en production)
SECRET_KEY = 'django-insecure-a*j8cnbo^w#-v-z14$u3ma4pf5_q-lko%kl@ih&#unyck3cy&n'

# Mode débogage (à désactiver en production)
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Applications installées
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # Requis pour django-allauth

    'rest_framework',
    'rest_framework_simplejwt',  # Pour JWT

    # Ordre important : 'users' avant 'allauth' et 'dj_rest_auth'
    'core',
    'users',  # Application pour la gestion des utilisateurs

    'allauth',  # Requis pour dj-rest-auth
    'allauth.account',  # Requis pour dj-rest-auth
    'allauth.socialaccount',  # Support pour les fonctionnalités sociales

    'dj_rest_auth',  # APIs d'authentification
    'dj_rest_auth.registration',  # Inscription

    'corsheaders',
    'gestion_immo',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # doit être avant CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # Requis pour django-allauth
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gestion_immo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Pour les templates email ou autres
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',  # obligatoire pour django-allauth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gestion_immo.wsgi.application'

# Base de données PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'baimmo',
        'USER': 'postgres',
        'PASSWORD': 'davou64598258',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Validation des mots de passe
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalisation
LANGUAGE_CODE = 'fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Fichiers statiques
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # Assure-toi que ce dossier existe physiquement
STATIC_ROOT = BASE_DIR / "staticfiles"

# Fichiers médias
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Type de champ de clé primaire par défaut
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Paramètres REST Framework
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': None,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',  # <-- autorise tout le monde sans authentification
    ],
}

# Configuration JWT
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'TOKEN_OBTAIN_SERIALIZER': 'rest_framework_simplejwt.serializers.TokenObtainPairSerializer',
}

# Paramètres dj-rest-auth
REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': None,
    'JWT_AUTH_REFRESH_COOKIE': None,
    'TOKEN_MODEL': None,
}

# Paramètres django-allauth
SITE_ID = 1  # Obligatoire

ACCOUNT_EMAIL_VERIFICATION = 'none'  # Pas de vérification mail en dev
ACCOUNT_SIGNUP_FIELDS = ['username', 'email', 'password1', 'password2']
ACCOUNT_LOGIN_METHODS = ['username']

# Configuration email - console pour dev
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = 'no-reply@localhost'

# Configuration CORS
CORS_ALLOW_ALL_ORIGINS = True  # Autorise toutes les origines
CORS_ALLOW_CREDENTIALS = True

# Liste blanche d’origines autorisées (utile si tu préfères restreindre)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    # Ajoute d'autres domaines/ports front si besoin
]

# Modèle utilisateur personnalisé
AUTH_USER_MODEL = 'users.CustomUser'
