from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ["*"]

# heroku用設定
DATABASES = {'default': dj_database_url.config()}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
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
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'root': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'django': {
            'handlers': ['null'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'serihu': {
            'handlers': ['null'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}
