from django import forms
from .models import Contact

# Create your forms here.


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ('first_name', 'last_name', 'email', 'message', 'subject')

	def __init__(self, *args, **kwargs):
		"""
		Add placeholders and classes, remove auto-generated
		labels and set autofocus on first field
		"""
		super().__init__(*args, **kwargs)
		
		self.fields['first_name'].widget.attrs['autofocus'] = True
