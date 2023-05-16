from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from cart.cart import Shipping, TotalPrice, Cart, Discount
from django.shortcuts import get_object_or_404
from order.models import Order
from django.conf import settings


# This function allows to send emails


def send_email(request, subject, template_name):
    order_id = request.session.get("order_id")
    order = get_object_or_404(Order, id=order_id)
    order.total_cost = order.get_total_cost(request)
    cart = Cart(request)
    discount = Discount(request.session)
    shipping = Shipping()
    total_price = TotalPrice(cart, discount, shipping)

    template = render_to_string(
        template_name,
        {"order": order, "shipping": shipping, "total_price": total_price},
    )
    subject_email = subject
    email = EmailMessage(
        subject_email,
        template,
        settings.EMAIL_HOST_USER,
        [order.email],
    )
    email.fail_silently = False
    email.send()
