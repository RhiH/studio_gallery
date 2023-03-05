from django.contrib import admin
from .models import ArtistsInfo, Category

# Register your models here.

admin.site.register(ArtistsInfo)
admin.site.register(Category)
