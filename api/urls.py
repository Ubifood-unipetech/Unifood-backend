from django.urls import include, path
from rest_framework import routers                  
from api.restaurants import Restaurants
from api.products import Products, ProductTypes
from api.authentication import Login

router = routers.DefaultRouter()      
router.register('restaurants',Restaurants)         
router.register('products', Products)
router.register('product/types', ProductTypes)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', Login.as_view(), name='token_obtain_pair')

]

