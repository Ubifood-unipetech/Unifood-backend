from django.contrib.gis.db import models
from django.contrib.auth.models import User,Group

# ---------------------------------------------------------
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=100)
    banner = models.ImageField(upload_to='restaurants/banners/', null=True, blank=True)
    coordinates = models.PointField()
    group = models.ForeignKey(Group, on_delete=models.PROTECT)
    cpfcnpj = models.CharField(max_length=14)

    class Meta:
        verbose_name = "restaurante"
        verbose_name_plural = "restaurantes"
        db_table = 'restaurants'


    def __str__(self):
        return self.name
    
# ---------------------------------------------------------
class ContactType(models.Model):
    name = models.CharField(max_length=50)
    mnemo = models.SlugField(max_length=20)
    icon = models.ImageField(upload_to='assets/contact/types/icons/',null=True, blank=True)

    class Meta:
        verbose_name = "tipo de contato"
        verbose_name_plural = "tipos de contatos"
        db_table = 'contacts_types'

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    type = models.ForeignKey(ContactType, on_delete=models.SET_NULL, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    input = models.CharField(max_length=50)

    class Meta:
        verbose_name = "contato"
        verbose_name_plural = "contatos"
        db_table = 'contacts'

    def __str__(self):
        return self.input

# ---------------------------------------------------------

class ProductType(models.Model):
    name = models.CharField(max_length=50)
    mnemo = models.SlugField(max_length=20)
    icon = models.ImageField(upload_to='assets/product/types/icons/', null=True, blank=True)

    class Meta:
        verbose_name = "tipo de produto"
        verbose_name_plural = "tipos de produtos"
        db_table = 'products_types'

    def __str__(self):
        return self.name
    

class Product(models.Model):
    type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    label = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='assets/product/images/')

    class Meta:
        verbose_name = "produto"
        verbose_name_plural = "produtos"
        db_table = 'products'

    def __str__(self):
        return self.label

# ---------------------------------------------------------

class Section(models.Model):
    name = models.CharField(max_length=50)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "secção"
        verbose_name_plural = "secções"
        db_table = 'sections'

    def __str__(self):
        return self.name

class SectionEntry(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "entrada de secção"
        verbose_name_plural = "entradas de secções"
        db_table = 'sections_entries'

# ---------------------------------------------------------

class Feedback(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "comentário"
        verbose_name_plural = "comentários"
        db_table = 'feedbacks'

    def __str__(self):
        return self.created_at
    
# ---------------------------------------------------------