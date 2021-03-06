from os import name, truncate
from typing import ChainMap
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Pict(models.Model):
    Main_pict = ImageField(upload_to='static/images/products')
    pict_1 = ImageField(upload_to='static/images/products')
    pict_2 = ImageField(upload_to='static/images/products')
    pict_3 = ImageField(upload_to='static/images/products')
    pict_4 = ImageField(upload_to='static/images/products')

class header(models.Model):
    header_pict = ImageField(upload_to='static/images/header')

class Category(models.Model):
    name = models.CharField(max_length=100)
    champaign = models.TextField(default='Input Champaign')
    description = models.TextField()
    # motto = models.TextField(default='Input Motto')
    # Header_pict = models.OneToOneField(header, on_delete=CASCADE)
    # headerimg = models.TextField(null=True)
    def __str__ (self):
        return(self.name)

class Product(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='static/images')
    # Pict = models.OneToOneField(Pict, on_delete=CASCADE)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=CASCADE)
    color = models.TextField()
    typeproducts = models.TextChoices('typeproducts', 'Normal Sale Limited')
    pricetype = models.CharField(blank=True, choices=typeproducts.choices, max_length=10)
    # typeproducts.choices
    # [('Limited', 'Limited'), ('Sale10', 'Sale 10'), ('Sale25', 'Sale 25') ('Sale50', 'Sale 50'), ('Sale70', 'Sale 70') ]
    def __str__ (self):
        return(self.name)

class account(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200, default='password')
    email = models.EmailField()
    def __str__ (self):
        return(self.name)

class Review(models.Model):
    account = models.ForeignKey(account, on_delete=CASCADE)
    Review = models.TextField()
    Product = models.ForeignKey(Product, on_delete=CASCADE)
    # def __str__ (self):
    #     return(account.name)






