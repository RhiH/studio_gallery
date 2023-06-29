from django.contrib import admin
from .models import Artists


# Register your models here.


class ArtistsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'country',
        'image',
    )


admin.site.register(Artists, ArtistsAdmin)
