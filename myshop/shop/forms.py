from django import forms
from .models import ProductRate, RATE


class RateForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), required=True)
    rate = forms.ChoiceField(choices=RATE, widget=forms.Select(), required=True)

    class Meta:
        model = ProductRate
        fields = ('text', 'rate')