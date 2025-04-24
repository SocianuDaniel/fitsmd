from .base import *
import environ

env = environ.Env()
# reading .env file
environ.Env.read_env()
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
STATIC_ROOT = os.path.join(BASE_DIR, env('STATIC_ROOT'))
ALLOWED_HOSTS = ['*']
