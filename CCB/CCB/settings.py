"""
Django settings for CCB project.

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
SECRET_KEY = '@n8a)&%9_3pd@8%&m=nc-md8gg)+6bq=ut@h77_^qmg20xn0=x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ADMINS = (('Ary Santos', 'aryfasa@gmail.com'), )

MANAGERS = ADMINS

ALLOWED_HOSTS = ['localhost']

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/'#'/CCB/listarProduto/' #/accounts/profile/

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compras',
    'bootstrapform',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'CCB.urls'

WSGI_APPLICATION = 'CCB.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'CCB',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
#STATICFILES_FINDERS = (
 #   "django.contrib.staticfiles.finders.FileSystemFinder",
  #  "django.contrib.staticfiles.finders.AppDirectoriesFinder"
#)
#TEMPLATE_LOADERS = (
 #   'django.template.loaders.filesystem.Loader',
  #  'django.template.loaders.app_directories.Loader',
#)

#TEMPLATE_DIRS = (
#    os.path.join(BASE_DIR, 'templates'),
#) 
#http://nullege.com/codes/show/src@t@i@tiote-0.2.4@tiote@forms@mysqlforms.py/61/django.forms.CheckboxSelectMultiple