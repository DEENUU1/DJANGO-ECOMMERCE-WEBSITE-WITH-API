from django.db import models
from django.utils.html import mark_safe

# Contact model
# Email, subject, text are required it's declared in 'contact.html'

SUBJECTS = [
    (1, 'Pytanie o produkt'),
    (2, 'Pytanie o zamówienie'),
    (3, 'Reklamacja'),
    (4, 'Inne'),
]


class Contact(models.Model):
    email = models.EmailField()
    subject = models.PositiveIntegerField(choices=SUBJECTS)
    text = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)


    def __int__(self):
        return self.subject
