from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey


class User(AbstractUser):
    pass

class Author(models.Model):
    pass

class Book(models.Model):
    Title = models.CharField(max_length=64)
    Description = models.CharField(max_length=400)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    PostedTime = models.DateTimeField(auto_now_add=True)
    Photo = models.URLField(max_length=1000, blank=True, null=True)
    Author = models.ManyToManyField(Author, on_delete=models.CASCADE, related_name='books')
    addedShoplist = models.ManyToManyField(User, blank=True, related_name='shoplist')
    Active = models.BooleanField(default=True)


class Order(models.Model):
    pass
