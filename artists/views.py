from django.shortcuts import render
from .models import Artists

# Create your views here.


def artists(request):

    artists = Artists.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    template = 'artists/artists.html'

    return render(request, template)
