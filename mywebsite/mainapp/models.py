from os import name
from typing import ChainMap
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__ (self):
        return(self.name)

class Product(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField()
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=CASCADE)
    color = models.TextField()
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
    def __str__ (self):
        return(self.number)






