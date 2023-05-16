from django.shortcuts import get_object_or_404
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from order.models import Order


# This signal allows to get information about order
# If order is paid the value in admin panel is changing to True
# It only works on the real page or after configuration the ngroku server on your local machine
def payment_notification(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        order = get_object_or_404(Order, id=ipn_obj.invoice)
        order.paid = True
        order.save()


valid_ipn_received.connect(payment_notification)
