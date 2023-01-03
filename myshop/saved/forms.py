from django import forms


class SavedAddProductForm(forms.Form):
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
