from rest_framework import serializers
from .models import Restaurant, Food
from django.contrib.auth.models import User

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ("pk",)
        
class restaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"
        read_only_fields = ("pk",)
    
    def to_representation(self,instance):
        foods = super().to_representation(instance)
        foods['foods'] = foodSerializer(Food.objects.filter(pk__in=instance.foods), many=True).data

        return foods

class foodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"
        read_only_fields = ("pk",)
