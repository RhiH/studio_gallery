from django.contrib import admin
from .models import Artists


# Register your models here.


class ArtistsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'biography',
    )


admin.site.register(Artists, ArtistsAdmin)
