from .base import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("DB_NAME"),
        'USER': env("DB_USER"),
        'PASSWORD': env("DB_PASS"),
        'HOST': env("DB_HOST"),
        'PORT': env("DB_PORT"),
    }
}
DEBUG=False
STATIC_ROOT = env('STATIC_ROOT')
ALLOWED_HOSTS = ['15.160.161.74','smdonline.net','www.smdonline.net']
SECURE_HSTS_SECONDS = 24*60*60
SECURE_SSL_REDIRECT  = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
