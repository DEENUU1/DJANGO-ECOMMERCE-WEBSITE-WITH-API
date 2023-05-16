from django.shortcuts import render
from .forms import ContactForm

# This view is responsible for contact form


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            file = request.FILES.get("file")
            form.instance.file = file
            form.save()
            return render(request, "contact_sent.html")
    else:
        form = ContactForm()
    return render(request, "contact_send.html", {"form": form})
