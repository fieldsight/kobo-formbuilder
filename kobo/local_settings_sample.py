import os
from pymongo import MongoClient

os.environ["DJANGO_SECRET_KEY"] = "@25)**hc^rjaiagb4#&q*84hr*uscsxwr-cv#0joiwj$))obyk11"


KOBOCAT_URL = 'http://localhost:8001'
KOBOCAT_INTERNAL_URL = 'http://localhost:8001'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        # 'NAME': 'sk1',
        'NAME': 'fkobo1',
        # 'NAME': 'kobolatest',
        # 'NAME': 'app_backup',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': '',
        'PORT': '',
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '@25)**hc^rjaiagb4#&q*84hr*uscsxwr-cv#0joiwj$))obyk11')
SESSION_COOKIE_NAME = 'f_cookie'
# SESSION_COOKIE_DOMAIN = "192.168.1.17" #None #'localhost'
SESSION_COOKIE_DOMAIN = 'localhost'

os.environ["ENKETO_VERSION"] = "Express"
ENKETO_URL = os.environ.get('ENKETO_URL', 'http://127.0.0.1:8005/')
ENKETO_SERVER = os.environ.get('ENKETO_URL') or os.environ.get('ENKETO_SERVER', 'http://127.0.0.1:8005/')
ENKETO_SERVER= ENKETO_SERVER + '/' if not ENKETO_SERVER.endswith('/') else ENKETO_SERVER
ENKETO_VERSION= os.environ.get('ENKETO_VERSION', 'Legacy').lower()
#assert ENKETO_VERSION in ['legacy', 'express']
ENKETO_PREVIEW_URI = 'webform/preview' if ENKETO_VERSION == 'legacy' else 'preview'
ENKETO_TOKEN = "enketorules"


DEFAULT_DEPLOYMENT_BACKEND = 'kobocat'

BROKER_URL = "redis://localhost:6379/0"

DEBUG = True

CORS_ORIGIN_WHITELIST = (

)

CORS_URLS_REGEX = r'^/assets/.*$'


MONGO_DATABASE = {
    'HOST': "127.0.0.1",
    'PORT': int(os.environ.get('KPI_MONGO_PORT', 27017)),
    'NAME': os.environ.get('KPI_MONGO_NAME', 'fformhub'),
    'USER': os.environ.get('KPI_MONGO_USER', ''),
    'PASSWORD': os.environ.get('KPI_MONGO_PASS', '')
}

if MONGO_DATABASE.get('USER') and MONGO_DATABASE.get('PASSWORD'):
    MONGO_CONNECTION_URL = (
        "mongodb://%(USER)s:%(PASSWORD)s@%(HOST)s:%(PORT)s") % MONGO_DATABASE
else:
    MONGO_CONNECTION_URL = "mongodb://%(HOST)s:%(PORT)s" % MONGO_DATABASE

MONGO_CONNECTION = MongoClient(
    MONGO_CONNECTION_URL, j=True, tz_aware=True, connect=False)
MONGO_DB = MONGO_CONNECTION[MONGO_DATABASE['NAME']]

