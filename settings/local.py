from settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'mycollegeai',
        'PASSWORD': 'mycollegeai',
        'HOST': 'mycollegeai-test.clssqwrmm6ld.us-east-2.rds.amazonaws.com',
        'PORT': 5432,
    }
}
