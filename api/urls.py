from django.urls import path, include
from .views import restaurantList, foodList, restaurantsListFilter, foodListFilter, userList
from rest_framework import routers                  # importar do rest_framework a biblioteca routers.

router = routers.SimpleRouter()                     # instanciar SimpleRouter().
router.register('restaurants', restaurantList)    # incluir no objeto um novo endereço.
router.register('foods', foodList)
router.register('users', userList)

urlpatterns = [
    path('',include(router.urls)),
    path('filters/foods/', foodListFilter.as_view()),
    path('filters/restaurants/', restaurantsListFilter.as_view())
]