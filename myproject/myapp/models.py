from django.db import models
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=100)
    
class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)