from django import forms
from .models import Order


# These forms are for complete order from card by adding
# every necessary information to order
# It's going to display fields like: first name, last name
# email, address, postal code and city
class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(label="Imie")
    last_name = forms.CharField(label="Nazwisko")
    phone_number = forms.CharField(label="Numer telefonu")
    address = forms.CharField(label="Adres")
    postal_code = forms.CharField(label="Kod pocztowy")
    city = forms.CharField(label="Miasto")

    class Meta:
        model = Order
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "address",
            "postal_code",
            "city",
        ]

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
