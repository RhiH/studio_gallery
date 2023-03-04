from django.db import models

# Create your models here.


class ArtistsCategory(models.Model):

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class ArtistsInfo(models.Model):
    creators = models.ForeignKey('', null=True,
            blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    biography = models.TextField()

    def __str__(self):
        return self.name
