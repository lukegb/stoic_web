"""
Django settings for stoic_web project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
import suit_config
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY','t-1bm#u1gcj#y0lxnh#_a=ihe$$4bg(-(*%&=(*#q=ya)q8drl')
if os.getenv('DJANGO_PRODUCTION',False)=='y':
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False
    TEMPLATE_DEBUG = False
    ALLOWED_HOSTS = ['.imperialcollege.tv']
else:
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True 
    TEMPLATE_DEBUG = True
    ALLOWED_HOSTS = ['.imperialcollege.tv']


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'south',
    'activelink',
    'debug_toolbar',
    'suit_redactor',
    'raven.contrib.django.raven_compat',
    'website',
)

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'stoic_web.urls'

WSGI_APPLICATION = 'stoic_web.wsgi.application'

# Set your DSN value
RAVEN_CONFIG = {
            'dsn':os.getenv('DJANGO_RAVEN', None),
            }

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DJANGO_DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.getenv('DJANGO_DB_NAME',os.path.join(BASE_DIR, 'db.sqlite3')),
	'USER': os.environ.get('DJANGO_DB_USER'),
	'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD'),
	'HOST': os.environ.get('DJANGO_DB_HOST'),
	'PORT': os.environ.get('DJANGO_DB_PORT'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = os.getenv('DJANGO_STATIC_URL', '/static/')
MEDIA_URL = os.getenv('DJANGO_MEDIA_URL' ,'/media/')
STATIC_ROOT=os.getenv('DJANGO_STATIC_DOC_ROOT', os.path.abspath("static_root"))
MEDIA_ROOT=os.getenv('DJANGO_MEDIA_ROOT', os.path.abspath("media_root"))
STATICFILES_DIRS= (
		os.path.abspath("static"),
)
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'django.core.context_processors.static',
)

TEMPLATE_DIRS = (
    BASE_DIR + '/templates/website'
)

INTERNAL_IPS = ('127.0.0.1',os.getenv('DJANGO_DEV_IP', '::1'),)

YOUTUBE_CHANNEL_ID = os.getenv('YOUTUBE_CHANNEL_ID', 'UCbnVV7tcJZlUJTh8zPQFxMQ')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
