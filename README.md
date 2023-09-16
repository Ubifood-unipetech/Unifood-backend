# Unifood
## Unifood-Backend

This is the codebase for the unifood's backend project created by Unipe's college students.

Unifood is an entrepreneurship project with the propose to create a menu of local restaurants. ~~Originally created based on the fact that we were trying to reach which 'coxinha' around our campus was more finatial viable.~~


This project works using these technologies:
- Django
- Django-Rest_Framework
- PostgresSQL
- Postgis
- ...more

## Installation
``` python
py -m venv venv  #Initialiaze virtual enviroment
cd /venv/Scripts
activate # or .\activate in case of powershell
cd ../..
pip install -r requirements.txt

# Set up a local postgres database and add postgis extension
# Create  a geospatial database and set the enviroment settings such as files,credentials on a settings.json file
# Read this for more info: https://docs.djangoproject.com/en/4.1/ref/contrib/gis/install/postgis/
```

## Settings.json file (This should be placed on the root of directory)
```json
{
    "DEBUG":true, 
    "GDAL_DATA":"/usr/share/gdal/",
    "PROJ_LIB":"/usr/share/proj/",
    "GDAL_LIBRARY_PATH":"/usr/lib/libgdal.so",
    "GEOS_LIBRARY_PATH":"/usr/local/lib/libgeos_c.so",
    "ALLOWED_HOSTS":["*"],
    "CORS_ORIGIN_ALLOW_ALL":true,
    "CORS_ALLOWED_ORIGINS":null,
    "DATABASES":{
        "default":{
            "ENGINE":"django.contrib.gis.db.backends.postgis",
            "NAME": "unifood",
            "USER": "unifood",
            "PASSWORD":"jailson123",
            "HOST": "localhost",
            "PORT": "5432"
        }
    },
    "MEDIA_URL":"media/",
    "MEDIA_ROOT":"/var/www/media/Unifood-backend/media/",
    "STATIC_URL":"static/",
    "STATIC_ROOT":"/var/www/static/static/",
    "STATICFILES_DIRS":["/var/www/static/Unifood-backend/static/"]  // Obs: if debug false your web server that will handle staticfiles dir
}
```

## Features

- CRUD RESTAURANTS
- CRUD PRODUCT
- Search filters + Pagination + Ordenation
- more...

## License

UNIPE

**Free Software, Hell Yeah!**
