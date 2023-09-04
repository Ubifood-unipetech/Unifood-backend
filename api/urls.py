from django.urls import include, path
from rest_framework import routers                  
from api.restaurant import Restaurants
from api.authentication import Login
router = routers.DefaultRouter()      
router.register('restaurants',Restaurants)         

urlpatterns = [
    path('', include(router.urls)),
    path('login/', Login.as_view(), name='token_obtain_pair')

]

