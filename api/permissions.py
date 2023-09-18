from rest_framework import permissions

class IsObjMember(permissions.DjangoModelPermissions):
    message = 'You need to be a member of obj group.'

    def has_object_permission(self, request, view, obj):
            if request.method not in permissions.SAFE_METHODS:
               return obj.group.user_set.contains(request.user)
            return True

class IsObjRestaurantMember(permissions.DjangoModelPermissions):
    message = 'You need to be a member of obj.restaurant group.'

    def has_object_permission(self, request, view, obj):
            if request.method not in permissions.SAFE_METHODS:
               return obj.restaurant.group.user_set.contains(request.user)
            return True