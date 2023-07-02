from django.contrib import admin
from .models import Artists


# Register your models here.


class ArtistsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'country',
        'image',
        'category',
    )


admin.site.register(Artists, ArtistsAdmin)
