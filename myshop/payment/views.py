from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from order.models import Order, OrderItem
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .email import send_email

# This view is displayed after successful payment
# This view also is sending email to the customer

@csrf_exempt
def payment_done(request):
    send_email(request,
               'Tu jest temat wiadomości',
               'emails/payment_done_email.html')

    return render(request,
                  'payment/done.html')

# This view is displayed after cancelled payment
# This view also is sending email to the customer

@csrf_exempt
def payment_canceled(request):
    send_email(request,
               'Tu jest temat wiadomości',
               'emails/payment_canceled_email.html')

    return render(request,
                  'payment/canceled.html')

# This view is displaying payment process
# It takes information from cart forwards them to PayPal API

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order,
                              id=order_id)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': order.get_total_cost(request),
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
                   'form': form})


