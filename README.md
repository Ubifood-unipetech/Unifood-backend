﻿# Unifood
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
# Create  a geospatial database and set the files on a settings.json file
# Read this for more info: https://docs.djangoproject.com/en/4.1/ref/contrib/gis/install/postgis/
```

## Settings.json file (This should be placed on the root of directory)
```json
{
    "DATABASES":{
        "default":{
            "ENGINE":"django.contrib.gis.db.backends.postgis",
            "NAME": "unifood",
            "USER": "postgres",
            "PASSWORD":"root",
            "HOST": "localhost", 
            "PORT": "5432"
        }
    },
    "GDAL_DATA":"C:\\Program Files\\PostgreSQL\\15\\gdal-data",
    "PROJ_LIB":"C:\\Program Files\\PostgreSQL\\15\\share\\contrib\\postgis-3.4\\proj",
    "GDAL_LIBRARY_PATH":"C:\\Program Files\\PostgreSQL\\15\\bin\\libgdal-33.dll",
    "GEOS_LIBRARY_PATH":"C:\\Program Files\\PostgreSQL\\15\\bin\\libgeos_c.dll"
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
