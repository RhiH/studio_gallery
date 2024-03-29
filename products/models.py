from django.db import models

# Create your models here.


class ProductArtist(models.Model):

    class Meta:
        verbose_name_plural = 'ProductArtists'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    identifier = models.CharField(max_length=5, null=True, blank=True)
    biography = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    artist = models.ForeignKey(
        'ProductArtist', null=True, blank=True, on_delete=models.SET_NULL
        )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
