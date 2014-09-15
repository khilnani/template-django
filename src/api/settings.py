"""
Django settings for api project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
ENV = os.environ['ENV']

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^duaw*bch_vuz+%fbt0!48vbydyie7*u1(jigm3&a5pdkvau$%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

# Config

from config import load_config

cfg = load_config()


# Application definition

INSTALLED_APPS = (
#    'django.contrib.admin',
#    'django.contrib.auth',
#    'django.contrib.sessions',
#    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'rest_framework',
    'rest_framework_swagger',
    'corsheaders',
    'sample',
)

MIDDLEWARE_CLASSES = (
#    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
#    'django.contrib.messages.middleware.MessageMiddleware',
#    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
)

ROOT_URLCONF = 'api.urls'

WSGI_APPLICATION = 'api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

if cfg.get('DB') == "sqlite":
  print "Using DB sqlite"
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
      }
  }
elif cfg.get('DB') == "postgresql":
  print "Using DB postgresql"
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql_psycopg2',
          'NAME': cfg.get('DB_NAME'),
          'USER': cfg.get('DB_USER'),
          'PASSWORD': cfg.get('DB_PASS'),
          'HOST': cfg.get('DB_HOST'),
          'PORT': cfg.get('DB_PORT'),
      }
  }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

CORS_ORIGIN_ALLOW_ALL = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)


REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.JSONPRenderer',
    ),
    'EXCEPTION_HANDLER': 'api.utils.custom_exception_handler',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'infologger': {
            'handlers': ['console'],
            'level': 'INFO',
            'formatter': 'verbose'
        }
    }
}

if ENV != "production":
  DEBUG = True
  TEMPLATE_DEBUG = True
  
  REST_FRAMEWORK = {
      'DEFAULT_RENDERER_CLASSES': (
          'rest_framework.renderers.JSONRenderer',
          'rest_framework.renderers.JSONPRenderer',
          'rest_framework.renderers.BrowsableAPIRenderer',
      )
  }

