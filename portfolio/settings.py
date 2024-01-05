"""
Django settings for portfolio project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import dj_database_url
import os
import cloudinary
import corsheaders
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =  os.environ.get("SECRET_KEY") 
#'django-insecure-!9+g&2rq2y&4oi2#u^756$itvd%#ql#82r*fbh5(eq#5mc@&+!'
#


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG","False").lower()=="true"
#True


ALLOWED_HOSTS =os.environ.get("ALLOWED_HOSTS").split(" ") 
#["portfolioapp-q7ra.onrender.com ", "127.0.0.1:8000",  "127.0.0.1"]
 
# 


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     'corsheaders',
    'rest_framework',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
     'corsheaders.middleware.CorsMiddleware',
     'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfolio',
        'USER': 'postgres',
        'PASSWORD': 'Shantanu8983@',
        'HOST': 'localhost',  # Set to your PostgreSQL server host
        'PORT': '5432',   
        # Set to your PostgreSQL server port
    }
}

database_url = os.environ.get("DATABASE_URL") 
#'postgres://portfolio_data_ar0w_user:JusyAtgVEg1yWMI6NJETCkBbpXptEOy3@dpg-cm8gpr8cmk4c7391v69g-a.oregon-postgres.render.com/portfolio_data_ar0w'
# 

DATABASES["default"] = dj_database_url.parse(database_url)

DATABASES['default']=dj_database_url.parse("postgres://portfolio_data_ar0w_user:JusyAtgVEg1yWMI6NJETCkBbpXptEOy3@dpg-cm8gpr8cmk4c7391v69g-a.oregon-postgres.render.com/portfolio_data_ar0w")


# settings.py

CLOUDINARY_URL = "cloudinary://935838691454949:2ZR0CSz_KyiZUN96SEmtB9Zwp7U@ddw1upvx3"

import cloudinary
import cloudinary.uploader
import cloudinary.api

# Cloudinary Configuration
cloudinary.config(
    cloud_name='ddw1upvx3',
    api_key='935838691454949',
    api_secret='2ZR0CSz_KyiZUN96SEmtB9Zwp7U',
)

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
    ('en', 'English'),  
    ('es', 'Spanish'), 
    ('fr', 'French'),
    ('hi', 'Hindi'),
]

TIME_ZONE = 'UTC'
USE_I18N = True

USE_TZ = True





# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


CORS_ALLOWED_ORIGINS = [
    "http://localhost:3001", 
    "http://localhost:3000", 
    "https://shantanus-resume.netlify.app"
]
