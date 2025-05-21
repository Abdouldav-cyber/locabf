"""
Paramètres Django pour le projet gestion_immo.

Généré par 'django-admin startproject' avec Django 5.2.1.

Pour plus d'informations sur ce fichier, voir
https://docs.djangoproject.com/en/5.2/topics/settings/

Pour la liste complète des paramètres et de leurs valeurs, voir
https://docs.djangoproject.com/en/5.2/ref/settings/
"""

from pathlib import Path
from datetime import timedelta

# Construire les chemins à l'intérieur du projet comme ceci : BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Paramètres de développement rapide - non adaptés à la production
# Voir https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# AVERTISSEMENT DE SÉCURITÉ : gardez la clé secrète utilisée en production secrète !
SECRET_KEY = 'django-insecure-a*j8cnbo^w#-v-z14$u3ma4pf5_q-lko%kl@ih&#unyck3cy&n'

# AVERTISSEMENT DE SÉCURITÉ : ne pas exécuter avec le mode débogage activé en production !
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Définition des applications
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
    'allauth',  # Requis pour dj-rest-auth
    'allauth.account',  # Requis pour dj-rest-auth
    'allauth.socialaccount',  # Support pour les fonctionnalités sociales
    'dj_rest_auth',  # APIs d'authentification
    'dj_rest_auth.registration',  # Inscription
    'corsheaders',
    'core',
    'psycopg2',  # Ajout pour PostgreSQL
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
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
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gestion_immo.wsgi.application'

# Base de données
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'basedav',  
        'USER': 'postgres',  
        'PASSWORD': 'davou64598258',  
        'HOST': 'localhost', 
        'PORT': '5432',  # Port par défaut de PostgreSQL
    }
}

# Validation des mots de passe
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalisation
# https://docs.djangoproject.com/en/5.2/topics/i18n/
LANGUAGE_CODE = 'fr'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Fichiers statiques (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
# Type de champ de clé primaire par défaut
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Fichiers médias
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Paramètres de REST Framework
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': None,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',  # Temporairement autoriser tout le monde
    ],
}

# Paramètres de Simple JWT
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'TOKEN_OBTAIN_SERIALIZER': 'core.serializers.MyTokenObtainPairSerializer',  # Ajout pour utiliser email
}

# Paramètres de dj-rest-auth
REST_AUTH = {
    'USE_JWT': True,
    'JWT_AUTH_COOKIE': None,
    'JWT_AUTH_REFRESH_COOKIE': None,
    'TOKEN_MODEL': None,
    'LOGIN_METHODS': ['email'],
}

# Paramètres pour django-allauth
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # Désactiver l'ancien paramètre
ACCOUNT_EMAIL_REQUIRED = False       # Désactiver l'ancien paramètre
ACCOUNT_USERNAME_REQUIRED = False    # Désactiver l'ancien paramètre

ACCOUNT_LOGIN_METHODS = ['email']    # Méthodes de connexion (remplace ACCOUNT_AUTHENTICATION_METHOD)
ACCOUNT_SIGNUP_FIELDS = ['email', 'password1', 'password2']  # Champs requis pour l'inscription

# Paramètres pour dj_rest_auth (facultatif, selon vos besoins)
REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'core.serializers.CustomRegisterSerializer',  # Si vous avez un sérialiseur personnalisé
}
# Paramètres CORS
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:53283",
    "http://127.0.0.1:53283",
]
CORS_ALLOW_CREDENTIALS = True

# Ajout de logging pour diagnostiquer les erreurs
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'dj_rest_auth': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}