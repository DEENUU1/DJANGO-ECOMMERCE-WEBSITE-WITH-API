from django import forms


# This form allows to add coupon in the cart
class CouponForm(forms.Form):
    code = forms.CharField()
