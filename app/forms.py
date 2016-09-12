from django import forms
from app.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=('name', 'email', 'subject', 'message')
