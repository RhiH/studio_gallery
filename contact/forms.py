from django import forms
from . models import Contact

# Create your forms here.

class ContactForm(forms.Form):
	first_name = forms.CharField(max_length = 75)
	last_name = forms.CharField(max_length = 75)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)