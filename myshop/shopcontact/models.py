from django.db import models

# Contact model
# Email, subject, text are required
# User is choosing message topics from the topics in variable SUBJECTS

SUBJECTS = [
    (1, "Pytanie o produkt"),
    (2, "Pytanie o zamówienie"),
    (3, "Reklamacja"),
    (4, "Inne"),
]


class Contact(models.Model):
    email = models.EmailField()
    subject = models.PositiveIntegerField(choices=SUBJECTS)
    text = models.TextField()
    file = models.FileField(
        blank=True,
        upload_to="media/contact_files/",
    )
    sent_date = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.subject
