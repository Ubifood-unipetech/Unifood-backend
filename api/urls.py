from django.urls import include, path
from rest_framework import routers                  
from api.restaurants import Restaurants
from api.products import Products, ProductTypes
from api.authentication import Login, Register, Logout

router = routers.DefaultRouter()      
router.register('restaurants',Restaurants)         
router.register('products', Products)
router.register('product/types', ProductTypes)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', Login.as_view(), name='token_obtain_pair'),
    path('register/', Register.as_view(), name='register_view'),
    path('logout/', Logout.as_view(), name='logout'),
]

