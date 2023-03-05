from django.db import models
from products.models import Category

# Create your models here.

class Creator(models.Model):
    name = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)

class Biography(models.Model):
    bio = models.CharField(max_length=200)
