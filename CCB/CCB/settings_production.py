# -*- coding: utf-8 -*-
from settings import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'CCB',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '',
        'PORT': '5432',
    }
}

ALLOWED_HOSTS = ['.ccbmoccompras.com.br']