"""
Django settings for flatgov project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import logging.config
from pathlib import Path
import os
from kombu import Queue
from dotenv import load_dotenv
load_dotenv(verbose=True)
from psycopg2cffi import compat
compat.register()
import subprocess
import flatgov

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
try:
    flatgov.__build__ = subprocess.check_output(["git", "describe", "--tags", "--always"], cwd=BASE_DIR).decode('utf-8').strip()
except:
    flatgov.__build__ = flatgov.__version__ + " ?"


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
try:
    SECRET_KEY = os.environ['SECRET_KEY']
except Exception as err:
    raise Exception("Set 'SECRET_KEY' as an environment variable") 


# SECURITY WARNING: don't run with debug turned on in production!
if os.getenv('DJANGO_SETTINGS_MODULE') == "flatgov.dev":
    DEBUG = True 
else:
    DEBUG = False 

ALLOWED_HOSTS = ['localhost', 'flatgov.linkedlegislation.com', 'plus.govtrack.us', 'billmap.govtrack.us']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'bills',
    'uscongress',

    'rest_framework',
    'django_tables2',
    'admin_auto_filters',

    'crs',  # by Dmitry
    'statementAdminPolicy',
    'committeeReport',
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

ROOT_URLCONF = 'flatgov.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates') 
        ],
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

WSGI_APPLICATION = 'flatgov.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CONGRESS_DATA_PATH = os.path.join(BASE_DIR, 'congress', 'data')
BILLS_JSON_PATH = os.path.join(BASE_DIR, 'json_data') 
RELATED_BILLS_JSON_PATH = os.path.join(BILLS_JSON_PATH, 'relatedBills.json') 
BILLS_META_JSON_PATH = os.path.join(BILLS_JSON_PATH, 'billsMeta.json') 
TITLES_INDEX_JSON_PATH = os.path.join(BILLS_JSON_PATH, 'titlesIndex.json') 


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATIC_URL = '/static/'


if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"


DJANGO_TABLES2_TEMPLATE = os.path.join(BASE_DIR, 'templates/django_tables2/table.html')
DJANGO_TABLES2_PAGINATE_BY = 10
DJANGO_TABLES2_STYLE = {
    'class': 'table table-striped table-bordered mb-0',
}


CELERY_BROKER_URL = 'redis://localhost:6379/0'
# CELERYD_TASK_SOFT_TIME_LIMIT = 1000
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_BACKEND = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
CELERY_DEFAULT_QUEUE = 'bill'
CELERY_QUEUES = (
    Queue('bill'),
)
CELERY_CREATE_MISSING_QUEUES = True
redbeat_redis_url = os.getenv('REDBEAT_REDIS_URL', CELERY_RESULT_BACKEND)


logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            # exact format is not important, this is the minimum information
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        '': {
            'level': 'WARNING',
            'handlers': ['console'],
        },
    },
})

BILL_SUMMARY_DEFAULT_TEXT = 'Bill Summary Default Text'

PROPUBLICA_CONGRESS_API_KEY = os.getenv('PROPUBLICA_CONGRESS_API_KEY', "")