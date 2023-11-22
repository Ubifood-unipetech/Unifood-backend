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
     "LEAFLET_CONFIG":{
        "DEFAULT_CENTER": [-7.1586642, -34.8537069],
        "DEFAULT_ZOOM": 16
    },
    "MEDIA_URL":"media/",
    "MEDIA_ROOT":"/var/www/media/Unifood-backend/media/",
    "STATIC_URL":"static/",
    "STATIC_ROOT":"/var/www/static/static/",
    "STATICFILES_DIRS":["/var/www/static/Unifood-backend/static/"],  // Obs: if debug false your web server that will handle staticfiles dir
    "JAZZMIN_SETTINGS":{
        "site_title": "Unifood Painel",
        "site_header": "Unifood",
        "site_brand": "Unifood",
        "site_logo": "jazzmin/img/logo.svg",
        "login_logo": "jazzmin/img/unifood_logo.svg",
        "login_logo_dark": "jazzmin/img/unifood_logo.svg",
        "site_logo_classes": "img-circle",
        "site_icon": "jazzmin/img/logo.svg",
        "welcome_sign": "Bem vindo",
        "copyright": "Unifood Ltd",
        "search_model": ["auth.User", "auth.Group"],
        "user_avatar": false,
        "show_sidebar": true,
        "navigation_expanded": true,
        "hide_apps": [],
        "hide_models": [],
        "order_with_respect_to": ["auth"],
        "custom_links": {
        },
        "icons": {
            "auth": "fas fa-users-cog",
            "auth.user": "fas fa-user",
            "auth.Group": "fas fa-users"
        },
        "default_icon_parents": "fas fa-chevron-circle-right",
        "default_icon_children": "fas fa-circle",
        "related_modal_active": false,
        "custom_css": "jazzmin/css/admin.css",
        "custom_js":  null,
        "use_google_fonts_cdn": true,
        "show_ui_builder": false,
        "changeform_format": "horizontal_tabs",
        "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"}
    },
    "JAZZMIN_UI_TWEAKS":{
        "navbar_small_text": false,
        "footer_small_text": false,
        "body_small_text": false,
        "brand_small_text": false,
        "brand_colour": "navbar-dark",
        "accent": "accent-primary",
        "navbar": "navbar-dark",
        "no_navbar_border": false,
        "navbar_fixed": false,
        "layout_boxed": false,
        "footer_fixed": false,
        "sidebar_fixed": false,
        "sidebar": "sidebar-dark-primary",
        "sidebar_nav_small_text": false,
        "sidebar_disable_expand": false,
        "sidebar_nav_child_indent": false,
        "sidebar_nav_compact_style": false,
        "sidebar_nav_legacy_style": false,
        "sidebar_nav_flat_style": false,
        "theme": "cyborg",
        "dark_mode_theme": "cyborg",
        "button_classes": {
            "primary": "btn-primary",
            "secondary": "btn-secondary",
            "info": "btn-outline-info",
            "warning": "btn-warning",
            "danger": "btn-danger",
            "success": "btn-success"
        },
        "actions_sticky_top": false
    }
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
