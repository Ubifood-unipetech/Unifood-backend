from rest_framework import viewsets
from rest_framework import serializers
from api.models import Restaurant
from rest_framework import permissions

class MemberOrAdmin(permissions.DjangoModelPermissions):
    message = 'Adding customers not allowed.'

    def has_object_permission(self, request, view, obj):
            return obj.organization.group.user_set.contains(request.user)


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
    permission_classes = [MemberOrAdmin]