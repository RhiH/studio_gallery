from django.shortcuts import render, get_object_or_404, HttpResponse


def index(request):
    template = 'contact/contact.html'

    return render(request, template)