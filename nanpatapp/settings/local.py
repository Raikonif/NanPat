from .develop import *

DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nanpatdb',
        'USER': 'developer',
        'PASSWORD': 'developer',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}


STATIC_URL = '/static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'