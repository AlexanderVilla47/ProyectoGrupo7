from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': "catalogo",
        'USER': "sa",
        'PASSWORD': "P741852963",
        'HOST': "localhost",
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server'
        },
    }
}
#####################################################################  