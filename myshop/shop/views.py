from django.shortcuts import render
from .models import Product, Category, Contact

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

        return render(request, 'contact.html')

    return render(request, 'contact.html')

