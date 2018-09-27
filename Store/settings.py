"""
Django settings for Store project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'llc80a8d1q^pqe#zovm1=32(y00%d%j!#9dpwb5sp70!cyhyz3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
#     'admin_langswitch',
    'wkhtmltopdf',
    'Charts',
    'Company',
    'MyUser',
    'Product',
    'StockDashboard',
    # 'escpos',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'Store.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR+'/templates/',True],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'Store.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

# MySQL
# CREATE DATABASE stocky DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;

DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     },
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': os.environ.get('MYSQL_DATABASE'),
        'USER': os.environ.get('MYSQL_USERNAME'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),        

        # 'NAME': 'stocky',
        # 'USER': 'root',
        # 'PASSWORD': 'root',
        # 'HOST': 'localhost',
        # 'PORT': '3306',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGES = (
             ('en-us', 'English'),
             ('ar', 'Arabic'),
            )

LANGUAGE_CODE = 'en-us'

LOCALE_PATHS = (
    os.path.join(BASE_DIR,'locale/'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


import logging.config

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%Y-%b-%d %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'ErrorFileHandler': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': (os.path.join( BASE_DIR, 'static/logs/errors.log')),
            'formatter':'verbose'
        },
        'DebugFileHandler': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': (os.path.join( BASE_DIR, 'static/logs/debug.log')),
            'formatter':'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers':['ErrorFileHandler'],
            'propagate': True,
            'level':'ERROR',
        },
        'DailyData': {
            'handlers': ['DebugFileHandler'],
            'level': 'DEBUG',
        },
    }
}

logging.config.dictConfig(LOGGING)



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def ABS_DIR(rel):
    return  os.path.join(BASE_DIR, rel.replace('/', os.path.sep))


STATIC_ROOT = ABS_DIR('static-root/')
MEDIA_ROOT= BASE_DIR+'/media-root/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

STATICFILES_DIRS = (
    ABS_DIR('static'),
)


AUTH_USER_MODEL = 'MyUser.User'

#  Xvfb :0 -screen 0 1024x768x16
# WKHTMLTOPDF_CMD = 'wkhtmltopdf --javascript-delay 4000'
WKHTMLTOPDF_CMD = 'wkhtmltopdf'



