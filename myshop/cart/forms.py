from django import forms
from .models import Order

# This form allows user to choose from 1 do 9 pieces of product
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 10)]
class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


# This forms is for complete order from card by adding 
# every necessary informations to order 
# It's gonna display fields like: first name, last name
# email, address, postal code and city 
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city']

    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        return instance
        

