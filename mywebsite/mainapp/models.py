from typing import ChainMap
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=CASCADE)

class Review(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    Review = models.TextField()
    Product = models.ForeignKey(Product, on_delete=CASCADE)




