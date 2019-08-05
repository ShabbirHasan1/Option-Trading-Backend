"""
Django settings for upstox_server project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", __file__)
import django_heroku
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "CHANGE_ME!!!! (P.S. the SECRET_KEY environment variable will be used, if set, instead)."

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    "scout_apm.django",
    "app",
    "background_task",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework_swagger"
]

SCOUT_MONITOR = True
SCOUT_KEY = "[ckVuP28u98MSeMhaJpgl]"
SCOUT_NAME = "TrakBit"

MIDDLEWARE = [
    "scout_apm.django.middleware.MiddlewareTimingMiddleware",
    "scout_apm.django.middleware.ViewTimingMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
ROOT_URLCONF = "upstox_server.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

redis_host = os.environ.get('REDIS_HOST', 'localhost')

# Channel layer definitions
# http://channels.readthedocs.io/en/latest/topics/channel_layers.html
'''
CHANNEL_LAYERS = {
    "default": {
        # This example app uses the Redis channel layer implementation channels_redis
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
             "hosts": [os.getenv('REDISTOGO_URL', 'redis://localhost:6379')],
        }
    },
}
'''

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "CONFIG": {
             "hosts": [os.getenv('REDISTOGO_URL', 'redis://localhost:6379')],
        }
    }
}


WSGI_APPLICATION = "upstox_server.wsgi.application"
#ASGI_APPLICATION = "upstox_server.routing.application"


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'trakbit',
        'USER': 'harsh',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '',
    }
}

DATABASE_URL = 'postgres://uskbcepgrhvnrx:25293de377423b780e80ddd06a653073c0f7e282c9f00b0d6490b489bff975a7@ec2-23-21-128-35.compute-1.amazonaws.com:5432/d4ct9loanaouam'
db_from_env = dj_database_url.config(conn_max_age=20)
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = "/static/"
django_heroku.settings(locals())