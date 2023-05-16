from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

# This function allows to send emails
def send_email(subject, template_name, username, email):
    template = render_to_string(template_name, {"username": username})
    subject_email = subject
    email = EmailMessage(
        subject_email,
        template,
        settings.EMAIL_HOST_USER,
        [email],
    )
    email.fail_silently = False
    email.send()
