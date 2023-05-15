from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Artists

# Create your views here.


def artists(request):
    template = 'artists/artists.html'

    return render(request, template)
