from django.db import models
from django.contrib.auth.models import User

from product.models import Products

class Order(models.Model):
    products = models.ManyToManyField(Products, blank = False)
    user    = models.ForeignKey(User, on_delete = models.CASCADE)