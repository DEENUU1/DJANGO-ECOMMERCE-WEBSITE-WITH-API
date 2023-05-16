from django import forms


# This form allows user to choose from 1 do 9 pieces of product
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 10)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label=""
    )
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
