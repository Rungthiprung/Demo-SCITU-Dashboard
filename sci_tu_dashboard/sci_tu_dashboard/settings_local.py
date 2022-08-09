import os
from pathlib import Path

DEBUG=True

BASE_DIR = Path(__file__).resolve().parent.parent

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'sci_dashboard_database',
        'USER': 'root',
        'PASSWORD': 'Rm-0123456789',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

#ICT_AUTH_APP_KEY = ''
