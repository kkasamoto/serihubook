from django.core.management.utils import get_random_secret_key

from .base import *


SECRET_KEY = get_random_secret_key()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True
ALLOWED_HOSTS = ["*"]

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[{asctime}]:{levelname}:{module}:Process{process:d}:Thread{thread:d}:{message}',
            'style': '{',
        },
        'simple': {
            'format': '[{asctime}]:{levelname}:{module}:{message}',
            'style': '{',
        },
    },
    'handlers': {
        'null': {
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'root': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'django': {
            'handlers': ['null'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['null'],
            'level': 'ERROR',
            'propagate': True,
        },
        'serihu': {
            'handlers': ['null'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}
