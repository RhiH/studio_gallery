from django.shortcuts import render
from .models import Artists

# Create your views here.


def artists(request):
    template = 'artists/artists.html'

    return render(request, template)
