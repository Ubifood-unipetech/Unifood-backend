from rest_framework import viewsets
from rest_framework import serializers
from api.models import Restaurant
from api.permissions import IsObjMember

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'desc', 'banner', 'coordinates']

class Restaurants(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing restaurants.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsObjMember]