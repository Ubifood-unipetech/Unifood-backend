from tkinter import CASCADE
from django.contrib.postgres.fields import ArrayField
from django.contrib.gis.db import models


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100, default="")
    desc = models.TextField(max_length=100, default='')
    coordinates = models.PointField(srid=4326)
    foods = ArrayField(models.IntegerField(), blank=True)
    feedback = models.FloatField(default=0.00)
    def __str__(self):
        return self.name
    
class Food(models.Model):
    owner = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default='0')
    name = models.CharField(max_length=100, default="")
    desc = models.TextField(max_length=100, default="")
    price = models.FloatField(default=0.00)
    feedback = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
    
    def delete(self):
        owner = Restaurant.objects.get(pk=self.owner.pk)
        if (self.pk) in owner.foods:
            owner.foods.remove(self.pk)
            owner.save()
        super().delete()

