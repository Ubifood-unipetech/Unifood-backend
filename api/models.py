from django.contrib.gis.db import models
from django.contrib.auth.models import User,Group

# ---------------------------------------------------------
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=100)
    banner = models.ImageField(upload_to='restaurants/banners/', null=True, blank=True)
    coordinates = models.PointField(srid=4326)

    def __str__(self):
        return self.name

class Organization(models.Model):
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)
    cpfcnpj = models.CharField(max_length=14)

    def __str__(self):
        return self.name
    
# ---------------------------------------------------------
class ContactType(models.Model):
    name = models.CharField(max_length=50)
    mnemo = models.SlugField(max_length=20)
    icon = models.ImageField(upload_to='assets/contact/types/icons/',null=True, blank=True)

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    type = models.ForeignKey(ContactType, on_delete=models.SET_NULL, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    input = models.CharField(max_length=50)

    def __str__(self):
        return self.input

# ---------------------------------------------------------

class ProductType(models.Model):
    name = models.CharField(max_length=50)
    mnemo = models.SlugField(max_length=20)
    icon = models.ImageField(upload_to='assets/product/types/icons/', null=True, blank=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    label = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='assets/product/images/')

    def __str__(self):
        return self.label

# ---------------------------------------------------------

class Section(models.Model):
    name = models.CharField(max_length=50)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SectionEntry(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

# ---------------------------------------------------------

class Feedback(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.PROTECT)
    comment = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.created_at
    
# ---------------------------------------------------------