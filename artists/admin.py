from django.contrib import admin
from .models import Artists, Category

# Register your models here.


class ArtistsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
    'friendly_name',
    'name',
    )


admin.site.register(Artists, ArtistsAdmin)
admin.site.register(Category, CategoryAdmin)

