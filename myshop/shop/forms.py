from django import forms
from .models import Comments

# This is a form to adding comments but it doesn't work yet

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('user_name', 'text', 'email', 'subject')
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
        }


