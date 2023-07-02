from django.shortcuts import render
from .models import Artists

# Create your views here.


def all_artists(request):

    artists = Artists.objects.all()

    context = {

        'artists': artists,
    }

    return render(request, 'artists/artists.html', context)
