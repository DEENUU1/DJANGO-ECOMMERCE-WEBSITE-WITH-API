from django import forms
from .models import Contact

# This form allows user to send messages
# they are stored in database
# Admin can read them in admin panel


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("email", "subject", "text", "file")
