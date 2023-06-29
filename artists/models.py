from django.db import models
from products.models import Product


# Create your models here.

class Artist(models.Model):

    class Meta:
        verbose_name_plural = 'Artists'

    category = models.ForeignKey(
        Product, null=True, blank=True, on_delete=models.SET_NULL
        )
    name = models.CharField(max_length=254)
    country = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
