"""
Django settings for ubifood project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import json

settings = 'settings.json'

with open(settings) as f:
    settings = json.loads(f.read())


# Postgis configuration
os.environ['GDAL_DATA'] = settings.get('GDAL_DATA')
os.environ['PROJ_LIB'] = settings.get('PROJ_LIB')
GDAL_LIBRARY_PATH = settings.get('GDAL_LIBRARY_PATH')
GEOS_LIBRARY_PATH = settings.get('GEOS_LIBRARY_PATH')


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = settings.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = settings.get('DEBUG')

ALLOWED_HOSTS = settings.get('ALLOWED_HOSTS')

CORS_ORIGIN_ALLOW_ALL = settings.get('CORS_ORIGIN_ALLOW_ALL')

if not CORS_ORIGIN_ALLOW_ALL:
    CORS_ALLOWED_ORIGINS = settings.get('CORS_ALLOWED_ORIGINS')

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'leaflet',
    'corsheaders',
    'rest_framework',
    'rest_framework_gis',
    'rest_framework_simplejwt',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = settings.get('DATABASES')

LEAFLET_CONFIG = settings.get('LEAFLET_CONFIG')

# Rest framework JWT authentication
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.DjangoModelPermissions',
    ],
    'DEFAULT_FILTER_BACKENDS': ['api.filters.JSONFilterBackend'],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images) and Media files 
# https://docs.djangoproject.com/en/4.1/howto/static-files/
# https://docs.djangoproject.com/en/4.2/topics/files/

MEDIA_URL = settings.get('MEDIA_URL')
MEDIA_ROOT = settings.get('MEDIA_ROOT')

STATIC_ROOT = settings.get('STATIC_ROOT')
STATIC_URL = settings.get('STATIC_URL')
STATICFILES_DIRS = settings.get('STATICFILES_DIRS')
JAZZMIN_SETTINGS = settings.get('JAZZMIN_SETTINGS')
JAZZMIN_UI_TWEAKS = settings.get('JAZZMIN_UI_TWEAKS')
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
