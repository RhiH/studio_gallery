from django.shortcuts import render
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_artists(request):
    """ A view that renders the artists page """

    return render(request, 'artists/artists.html')
