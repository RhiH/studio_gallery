from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import ContactForm

def contact(request):
    """ contact page """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message')
        else:
            messages.error(request, 'Failed to send message. Please ensure the form is valid.')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }
    
    return render(request, template, context)