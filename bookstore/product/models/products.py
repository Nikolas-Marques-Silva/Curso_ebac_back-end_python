from django.db import models

class Products(models.Model):
    id          = models.AutoField(primary_key=True, unique= True)
    title       = models.CharField(max_length = 100)
    description = models.TextField(max_length = 500, blank =True, null = True)
    price       = models.PositiveIntegerField(null = True)
    ative       = models.BooleanField(default = True)
    category    = models.ManyToManyField('product.Category', blank = True)