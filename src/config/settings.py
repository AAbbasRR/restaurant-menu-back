from pathlib import Path
from decouple import config

import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['*', ]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd party apps
    'corsheaders',
    'rest_framework',
    # local apps
    'app_menu'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # cors-headers
    'corsheaders.middleware.CorsMiddleware',
    # multi language
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
SQL_LITE_DATABASE = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
}

if config('USE_MYSQL', default=False, cast=bool):
    MYSQL_DATABASE = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('MYSQL_NAME'),
        'USER': config('MYSQL_USER'),
        'PASSWORD': config('MYSQL_PASS'),
        'HOST': config('MYSQL_HOST'),
        'PORT': config('MYSQL_PORT', cast=int),
    }

if config('USE_POSTGRES', default=False, cast=bool):
    POSTGRE_SQL_DATABASE = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('POSTGRES_NAME'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASS'),
        'HOST': config('POSTGRES_HOST'),
        'PORT': config('POSTGRES_PORT', cast=int),
    }

DEFAULT_DATABASE = config('DEFAULT_DATABASE_NAME', default="")

DATABASES = {
    'default': SQL_LITE_DATABASE if DEBUG else MYSQL_DATABASE if DEFAULT_DATABASE.upper() == "MYSQL" else POSTGRE_SQL_DATABASE if DEFAULT_DATABASE.upper() == "POSTGRESQL" else SQL_LITE_DATABASE
}

# Password validation
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

# ___django settings___ #
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = 'src/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'src/static/')
# Media files (Images, Files)
MEDIA_URL = 'src/media/'
MEDIA_ROOT = (
    os.path.join(BASE_DIR, 'src/media')
)
# Internationalization
LANGUAGES = (
    ('fa', 'Persian'),
)
DEFAULT_LANGUAGE = 1
LANGUAGE_CODE = 'fa'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# __django multi language settings__ #
LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]

# ___Request Api Options___ #
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_REGEX_WHITELIST = ['*', ]
