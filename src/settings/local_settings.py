import os


DEBUG = True
LOG_ROOT = os.environ.get("LOG_ROOT")
LOG_FILENAME = "{}.log".format(os.environ.get("APPLICATION_NAME"))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
        }
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'encoding': 'utf-8',
            'filename': os.path.join(LOG_ROOT, LOG_FILENAME)
        }
    },
    'loggers': {
        'default': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propogate': True,
        }
    }
}


CELERY_BROKER_URL = 'redis://broker:6379/0'
CELERY_RESULT_BACKEND = 'redis://broker:6379/0'
