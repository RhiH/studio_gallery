from django.db import models
from products.models import Category, Product


# Create your models here.

class Artists(models.Model):

    class Meta:
        verbose_name_plural = 'Artists'

    category = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    artist = models.CharField(max_length=254)
    biography = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
