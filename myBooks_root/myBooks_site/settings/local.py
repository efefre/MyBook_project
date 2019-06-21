from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't#j&!je%gq_2$=szo*z&7-6pby1+$088&w$dq6kfdy^jpen@ub'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ROOT_URLCONF = 'myBooks_site.urls'

WSGI_APPLICATION = 'myBooks_site.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}