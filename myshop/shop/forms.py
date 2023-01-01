from django import forms
from .models import ProductRate, RATE


# This form allows user to choose rate from 1 to 5
# Write a comment of the product
# All fields are required to save
class RateForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), required=True)
    rate = forms.ChoiceField(choices=RATE, widget=forms.Select(), required=True)

    class Meta:
        model = ProductRate
        fields = ('text', 'rate')


# This form allows user to filter products
# User should be able to choose filtering by: price, name

class ProductsFilterForm(forms.Form):
    name = forms.CharField()


# This form allows user to filter rates
# User should be able to choose filtering by: date, rate


class ProductRateFilterForm(forms.Form):
    name = forms.CharField()
