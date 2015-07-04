"""
Django settings for destination project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from oscar import get_core_apps, OSCAR_MAIN_TEMPLATE_DIR

PROJECT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

location = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)), x)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'uf6r+p)-231*!9!&(11doto!-@m)t89s+e-czbe-%)6durti1o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
SITE_ID = 1
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []
ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
ROOT_URLCONF = 'urls'


TEMPLATE_DIRS = (
    location('templates'),
    OSCAR_MAIN_TEMPLATE_DIR,
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

PROJECT_ROOT = os.path.dirname(__file__) + "/"
DEFAULT_URL = 'http://destination.dev:8000'
#STATIC_URL = '/static/'
STATIC_URL = 'http://static.destination.dev/'
MEDIA_ROOT = location("static/media/")
MEDIA_URL = 'media/'
STATICFILES_DIRS = ()
STATIC_ROOT = location('static/')
LOCALE_PATHS = (PROJECT_ROOT + "/locale/",)
GEOIP_PATH = os.path.join(os.path.dirname(__file__), 'geoip')
from oscar.defaults import *

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

LOG_ROOT = location('logs')
# Ensure log root exists
if not os.path.exists(LOG_ROOT):
    os.mkdir(LOG_ROOT)	
	
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'oscar.apps.search.context_processors.search_form',
    'oscar.apps.promotions.context_processors.promotions',
    'oscar.apps.checkout.context_processors.checkout',
    'oscar.apps.customer.notifications.context_processors.notifications',
    'oscar.core.context_processors.metadata',
)

# Application definition
INSTALLED_APPS = [
	'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'django.contrib.flatpages',
	
	# Oscar dependencies
	'compressor',
	#'south',
	
	# External apps
	#'haystack',
	#'sorl.thumbnail',
]
INSTALLED_APPS = INSTALLED_APPS + get_core_apps()

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
	
	'oscar.apps.basket.middleware.BasketMiddleware',
)

try:
    from settings_local import *
except ImportError:
    pass