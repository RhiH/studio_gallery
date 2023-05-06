from django.contrib import admin
from .models import Creator

# Register your models here.


class CreatorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'biography,'
    )


admin.site.register(Creator, CreatorAdmin)
