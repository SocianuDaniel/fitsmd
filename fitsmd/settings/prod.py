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

#-------------aws bucket config------------------------------------

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
   },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage"
    },
}




AWS_ACCESS_KEY_ID = env("AWS_S3_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_S3_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = "eu-south-1"

AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com"

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_ROOT = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
MEDIA_ROOT = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"


#-------------end bucket config------------------------------------
