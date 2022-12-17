from django.shortcuts import render
from .models import Contact

# Django view for contact
# On url = x.x.x.x/contact it should display contact form
# After clicking button 'SUBMIT' it moves the user to 'contact_sent.html'
# Data go to admin panel, they are kept in SQLite as everything.
# If contact has not been sent it's return to contact form.

def contact(request):
    if request.method=='POST':
        contact=Contact()
        subject=request.POST.get('subject')
        email=request.POST.get('email')
        text=request.POST.get('text')

        contact.subject=subject
        contact.email=email
        contact.text=text
        contact.save()

        return render(request, 'contact_sent.html')

    return render(request, 'contact.html')