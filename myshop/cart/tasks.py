from celery import shared_task
from celery import Celery
from django.core.mail import send_mail
from .models import Order


# This function allows to send email after completing the order
# The content of the email is in this code. You can change it if you want
@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Zamówienie nr {order.id}'
    message = f'Witaj, {order.first_name} \n\n dziękujemy za złożenie zamówienia w naszym sklepie.\'' \
              f'Twój numer zamówienia to: {order.id}'

    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.email])
    return mail_sent
