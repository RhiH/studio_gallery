from django.contrib import admin
from .models import ArtistsInfo, ArtistsCategory

# Register your models here.

admin.site.register(ArtistsInfo)
admin.site.register(ArtistsCategory)
