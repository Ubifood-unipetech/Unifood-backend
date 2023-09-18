from django.contrib import admin
from api.models import Restaurant, Product, ProductType, Contact, ContactType
from leaflet.admin import LeafletGeoAdmin


admin.site.register(Restaurant, LeafletGeoAdmin)
admin.site.register(Contact)
admin.site.register(ContactType)
admin.site.register(Product)
admin.site.register(ProductType)