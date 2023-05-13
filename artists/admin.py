from django.contrib import admin
from .models import Artists


# Register your models here.


class ArtistsAdmin(admin.ModelAdmin):
    list_display = (
        'artist',
        'biography',
    )


admin.site.register(Artists, ArtistsAdmin)
