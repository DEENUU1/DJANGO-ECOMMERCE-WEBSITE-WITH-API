from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart, Discount, Shipping, TotalPrice
from cart.forms import CartAddProductForm
from coupons.forms import CouponForm


# This view represents adding to cart function


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd["quantity"], update_quantity=cd["update"])

    return redirect("cart:cart_detail")


# This view represent remove from cart option


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("cart:cart_detail")


# This view represent the whole cart


def cart_detail(request):
    cart = Cart(request)
    discount = Discount(request.session)
    shipping = Shipping()
    total_price = TotalPrice(cart, discount, shipping)
    coupon_discount = discount.get_discount(total_price.get_total_price())

    for item in cart:
        item["update_quantity_form"] = CartAddProductForm(
            initial={"quantity": item["quantity"], "update": True}
        )

    coupon_apply_form = CouponForm()

    return render(
        request,
        "cart/cart_details.html",
        {
            "cart": cart,
            "coupon_apply_form": coupon_apply_form,
            "discount": discount,
            "shipping": shipping,
            "total_price": total_price,
            "coupon_discount": coupon_discount,
        },
    )
