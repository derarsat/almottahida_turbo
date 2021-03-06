from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@a)iglg()m#tg%iob)zjuk5i$$x(a+f&*$a%89-!jas_w$z--#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Application definition
CRISPY_TEMPLATE_PACK = 'bootstrap4'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'product',
    'users',
    "corsheaders",
    'home'

]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'turbo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'turbo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    #     'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'test_almottahida',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True,
        },
    }
    # hn
    # 'default': {
    #     'ENGINE': 'mysql.connector.django',
    #     'NAME': 'almomjgn_accounting_database_3',
    #     'USER': 'almomjgn_accounting_user',
    #     'PASSWORD': 'TITNDPildvm7050@!',
    #     'HOST': 'localhost',
    #     'PORT': '3306',
    #     'OPTIONS': {
    #         'autocommit': True,
    #     },
    # }
    # This is master
    # 'default': {
    #     'ENGINE': 'mysql.connector.django',
    #     'NAME': 'almomjgn_accounting_database',
    #     'USER': 'almomjgn_accounting_user',
    #     'PASSWORD': 'TITNDPildvm7050@!',
    #     'HOST': 'localhost',
    #     'PORT': '3306',
    #     'OPTIONS': {
    #         'autocommit': True,
    #     },
    # }
    # Test
    # 'default': {
    #     'ENGINE': 'mysql.connector.django',
    #     'NAME': 'almomjgn_test',
    #     'USER': 'almomjgn_accounting_user',
    #     'PASSWORD': 'TITNDPildvm7050@!',
    #     'HOST': 'localhost',
    #     'PORT': '3306',
    #     'OPTIONS': {
    #         'autocommit': True,
    #     },
    # }
    # THis is syrian
    # 'default': {
    #     'ENGINE': 'mysql.connector.django',
    #     'NAME': 'almomjgn_accounting_database_2',
    #     'USER': 'almomjgn_accounting_user',
    #     'PASSWORD': 'TITNDPildvm7050@!',
    #     'HOST': 'localhost',
    #     'PORT': '3306',
    #     'OPTIONS': {
    #         'autocommit': True,
    #     },
    # }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
ALLOWED_HOSTS = ["almottahida.org", "127.0.0.1", "accounting.almottahida.org", "sy.accounting.almottahida.org","hn.almottahida.org","test.almottahida.org"]
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
LOGIN_URL = '/users/login'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = "/static/"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')  # 'data' is my media folder
MEDIA_URL = '/media/'
CORS_ALLOW_ALL_ORIGINS = True
