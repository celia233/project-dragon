"""
Django settings for dragon project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os, warnings

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get('DRAGON_SECRET_KEY')
if SECRET_KEY == None:
    warnings.warn("No secret key found, using public default")
    SECRET_KEY = '$rbe#s_2)bih1pyp*$bwx%du#!b($(bugv!g@92au9@!hia&e$'


# SECURITY WARNING: don't run with debug turned on in production!
debug_var = os.environ.get('DRAGON_DEBUG')

DEBUG = debug_var == "True" if debug_var is not None else True

if DEBUG:
    warnings.warn("Using debug mode")

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'library.apps.LibraryConfig',
    'members.apps.MembersConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'dragon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'dragon/templates')],
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

WSGI_APPLICATION = 'dragon.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

use_mysql = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dragon',
        'USER': 'dungeonmaster',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306'
    }
} if use_mysql else {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dragon.sqlite3'
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 8,}
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    #{   'NAME': 'registration.validators.CustomPasswordValidator',},
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/dragon/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'dragon/static')
]
