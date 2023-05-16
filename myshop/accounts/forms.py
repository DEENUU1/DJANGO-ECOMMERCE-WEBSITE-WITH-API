from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


# Form for registration
# Display fields like: username, email, password1, password2
# password1 and 2 have to be the same to complite the form


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# Form for password reset
# Display fields like email and password


class PasswordResetForm(forms.Form):
    email = forms.EmailField()
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)


# Form for deleting account
# Display fields like email and password


class DeleteUserForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
