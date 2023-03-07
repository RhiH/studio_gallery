from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Creator
from products.models import Category

def artists(request):
    template = 'artists/artists.html'

    return render(request, template)
