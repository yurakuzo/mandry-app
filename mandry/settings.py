import os
from pathlib import Path
from mandry.config import Config as cfg

import dj_database_url


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = cfg.SECRET_KEY.value

DEBUG = cfg.DEBUG.value

ALLOWED_HOSTS = cfg.ALLOWED_HOSTS.value

CORS_ORIGIN_ALLOW_ALL = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',

    'traveller',
    'trip',
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
ROOT_URLCONF = 'mandry.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mandry.wsgi.application'

if DEBUG:
    # Development database configuration
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': cfg.POSTGRES_DB.value,
            'USER': cfg.POSTGRES_USER.value,
            'PASSWORD': cfg.POSTGRES_PASSWORD.value,
            'HOST': cfg.POSTGRES_HOST.value,
            'PORT': cfg.POSTGRES_PORT.value,
        }
    }
else:
    # Production database configuration
    DATABASES = {
        'default': dj_database_url.config(
            default=cfg.POSTGRES_EXTERNAL_URL.value,
            conn_max_age=600
        )
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

AUTH_USER_MODEL = 'traveller.Traveller'
LOGOUT_REDIRECT_URL = 'main_page'
LOGIN_REDIRECT_URL = 'main_page'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = 'static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
