"""
Zadanie zaliczeniowe z języka Python  
Imię i nazwisko ucznia: Tomasz Gradowski
Data wykonania zadania: 19.05.2025
Treść zadania: Sprzedaż biletów w kinie  
Opis funkcjonalności aplikacji: Konfiguracja ustawień Django, w tym bazy danych, mediów, aplikacji oraz ustawień bezpieczeństwa i lokalizacji.
"""

import os
from pathlib import Path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django-insecure-rq3c-el3x#4jkilkr)kontju7+mv^@ennwi#1r=t20a==l6z!-'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'kino',  # Dodano aplikację kino
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'absolutne_kino.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Dodano ścieżkę do katalogu templates
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',  # Dodano kontekst do obsługi plików multimedialnych
            ],
        },
    },
]

WSGI_APPLICATION = 'absolutne_kino.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'

MEDIA_URL = '/media/'  # Dodano adres URL do plików multimedialnych (np. obrazy filmów)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Dodano lokalną ścieżkę do przechowywania multimediów

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
