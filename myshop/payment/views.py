from decimal import Decimal
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from cart.models import Order, OrderItem
from django.views.decorators.csrf import csrf_exempt
from cart.cart import Cart
from paypal.standard.ipn.models import PayPalIPN


def shipping_value():
    return Decimal('8.99')


@csrf_exempt
def payment_done(request):
    return render(request, 'payment/done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'payment/canceled.html')


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    host = request.get_host()
    cart = Cart(request)

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': order.get_total_cost(),
        'shipping': 8.99,
        'item_name': order.id,
        'invoice': str(order.id),
        'currency_code': 'PLN',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('payment:done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('payment:canceled')),

    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment/process.html',
                  {'order': order,
                   'form': form,
                   'cart': cart, })
