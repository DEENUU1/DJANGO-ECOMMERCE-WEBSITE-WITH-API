from django.db import models

# Contact model
# Email, subject, text are required it's declared in 'contact.html'

class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    text = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
