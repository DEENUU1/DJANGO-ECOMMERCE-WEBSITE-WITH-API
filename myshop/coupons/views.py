from django.shortcuts import redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Coupon
from .forms import CouponForm


# This view is checking if the coupon added in cart is available


@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data["code"]
        try:
            coupon = Coupon.objects.get(
                code__iexact=code, valid_from__lte=now, valid_to__gte=now, active=True
            )

            request.session["coupon_id"] = coupon.id
        except:
            pass

    return redirect("cart:cart_detail")
