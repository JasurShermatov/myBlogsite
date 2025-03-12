import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


from dotenv import load_dotenv

load_dotenv(".env")
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = True


ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main_app",  # added by me
    'widget_tweaks'
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "blogsite.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "blogsite.wsgi.application"

import os

# Loyihangizning asosiy papkasini aniqlang
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Media fayllar joylashuvi
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

import os
from pathlib import Path
from dotenv import load_dotenv

# Bazaviy papka yo‘lini olish
BASE_DIR = Path(__file__).resolve().parent.parent

# .env faylni yuklash
load_dotenv(os.path.join(BASE_DIR, ".env"))

# Database sozlamalarini .env dan olish
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DB_NAME", "postgres"),
        "USER": os.getenv("DB_USER", "postgres"),
        "PASSWORD": os.getenv("DB_PASSWORD", "postgres"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "default_option")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "default_option")
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", "default_option")
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = "smtp.gmail.com"
