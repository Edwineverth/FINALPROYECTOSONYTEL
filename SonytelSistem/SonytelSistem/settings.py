"""
Django settings for SonytelSistem project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ai)!8f!4ha(-mfdhx$td=ch)r#ls-alwygxk45ap#_hg1x)-3$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

from unipath import Path 
RUTA_PROYECTO= Path(__file__).ancestor(2)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'crispy_forms',
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.sistema',
    'apps.articulos',
    'apps.facturadetallle',
    'apps.mantenimiento',
    'bootstrap3',
    'table',

)
CRISPY_TEMPLATE_PACK = 'bootstrap3'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'SonytelSistem.urls'

WSGI_APPLICATION = 'SonytelSistem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
#Sonytelproject
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Sonytelproject',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5433',
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-EC'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#SE ESTABLECE ESTA VARIABLE PARA HACER REFERENCIA A LA CARPETA DONDE SE ALMACENARA TODAS LAS IMAGENES
MEDIA_ROOT =RUTA_PROYECTO.child('media')
#SE HACE REFERENCIA AL ALMACEN DE CARPETAS MEDIA
MEDIA_URL='http://127.0.0.1:8000/media/'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
from django.core.urlresolvers import reverse_lazy
LOGIN_URL=reverse_lazy('login')
LOGIN_REDIRECT_URL= reverse_lazy('sistema')
LOGOUT_URL=reverse_lazy('logout')


STATIC_URL = '/static/'
STATICFILES_DIRS=(
    RUTA_PROYECTO.child('static')),
TEMPLATE_DIRS=(
    RUTA_PROYECTO.child('templates')),
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)