from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# This view is responsible for displaying page with information about shop
def about(request):
    return render(request, 'about.html')

# This view is responsible for statute of the shop

def statute(request):
    return render(request, 'statute.html')

# This view is responsible for shop privacy and policy

def privacy_policy(request):
    return render(request, 'privacy.html')

# This view is responsible for shipping information

def shipping(request):
    return render(request, 'shipping.html')

# This view is responsible for returns information

def returns_complaints(request):
    return render(request, 'returns.html')

# This view is responsible for FAQ of the shop

def faq(request):
    return render(request, 'faq.html')

# This view is responsible for displaying all available APIs
# Only registered users are able to get this page

@user_passes_test(lambda u: u.is_superuser)
def main_api(request):
    return render(request, 'main_api.html')
