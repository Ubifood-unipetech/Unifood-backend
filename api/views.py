from rest_framework import viewsets
from rest_framework import generics, status
from django.http import JsonResponse
from rest_framework.response import Response
from django.db.models import Q
from .models import Restaurant, Food
from .serializers import restaurantSerializer, foodSerializer, userSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
#Restaurantes 
class restaurantList(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()           
    serializer_class = restaurantSerializer

#Comidas 
class foodList(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = foodSerializer

#Users
class userList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer
    permission_classes = [IsAdminUser]

#Restaurants filters
class restaurantsListFilter(generics.GenericAPIView):
    queryset = Restaurant
    serializer_class = restaurantSerializer

    def get(self, request):
        name = request.GET.get('name', '')
        desc = request.GET.get('desc', '')
        feedback = request.GET.get('feedback', '')
        try:
            queryset = self.queryset.objects.filter(Q(name__icontains=name), Q(desc__icontains=desc), Q(feedback__icontains=feedback))
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        except:
            return JsonResponse({},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#Comidas filters
class foodListFilter(generics.GenericAPIView):
    queryset = Food
    serializer_class = foodSerializer

    def get(self, request):
        name = request.GET.get('name', '')
        desc = request.GET.get('desc', '')
        price = request.GET.get('price', '')
        feedback = request.GET.get('feedback', '')
        try:
            queryset = self.queryset.objects.filter(Q(name__icontains=name), Q(desc__icontains=desc),Q(price__icontains=price), Q(feedback__icontains=feedback))
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        except:
            return JsonResponse({},status=status.HTTP_500_INTERNAL_SERVER_ERROR)