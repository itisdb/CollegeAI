from settings.base import *

DEBUG = True

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

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'mycollegeai',
#         'USER': 'XXX',
#         'PASSWORD': 'XXXX',
#         'HOST': 'https://IP/',
#         'PORT': 5432
#     }
# }