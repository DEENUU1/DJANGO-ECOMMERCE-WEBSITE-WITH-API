from django import forms


# This form allows to add coupon with rabat
class CouponForm(forms.Form):
    code = forms.CharField()