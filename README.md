# Ubifood
## Ubifood-Backend
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

This is the codebase for the ubifood's backend project created by Unipe's college students.

Ubifood is an entrepreneurship project with the propose to create a menu of local restaurants. ~~Originally created based on the fact that we were trying to reach which 'coxinha' around our campus was more finatial viable.~~


This project works using these technologies:
- Django
- Django-Rest_Framework
- Postgis
- ...more

## Installation
``` python
py -m venv venv  #Initialiaze virtual enviroment
cd /venv/Scripts
activate # or .\activate in case of powershell
cd ../..
pip install -r requirements.txt

# set up a local postgres database and add postgis extension
# Read this for more info: https://docs.djangoproject.com/en/4.1/ref/contrib/gis/install/postgis/
```
## Features

- CRUD RESTAURANTS
- CRUD FOODS
- CRUD USERS
- Search filters + pagination
- more...

## License

UNIPE

**Free Software, Hell Yeah!**
