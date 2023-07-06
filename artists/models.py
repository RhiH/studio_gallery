from django.db import models

from products.models import ProductArtist

# Create your models here.


class Artists(models.Model):

    name = models.CharField(max_length=254)
    country = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    product_artist = models.ForeignKey(
        ProductArtist, null=True, blank=True, on_delete=models.SET_NULL
        )

    def __str__(self):
        return self.name
