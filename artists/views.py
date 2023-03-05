from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse



def index(request):
    template = 'artists/artists.html'

    return render(request, template)
