from settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mycollegeai_read',
        'USER': 'mycollegeai',
        'PASSWORD': 'mycollegeai',
        'HOST': '101.53.146.142',
        'PORT': 5432
    }
}
'''