from django.db import models
from products.models import Category

# Create your models here.


#class Creator(models.Model):
#    name = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)

# class Biography(models.Model):
#   bio = models.CharField(max_length=200)


# Create your models here.
# class Category(models.Model):

#     class Meta:
#         verbose_name_plural = 'Categories'

 #    name = models.CharField(max_length=254)
#     friendly_name = models.CharField(max_length=254, null=True, blank=True)

#     def __str__(self):
#         return self.name

#     def get_friendly_name(self):
#         return self.friendly_name


class Artists(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)
    biography = models.CharField(max_length=500)

    def __str__(self):
        return self.name
