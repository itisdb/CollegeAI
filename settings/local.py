from settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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
