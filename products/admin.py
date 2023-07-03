from django.contrib import admin
from .models import Product, ProductArtist

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'artist',
        'price',
        'image',
        'description'
    )

    ordering = ('sku',)


class ProductArtistAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductArtist, ProductArtistAdmin)
