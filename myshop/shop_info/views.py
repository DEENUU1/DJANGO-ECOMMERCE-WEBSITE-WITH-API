from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# This view is to display page with information about shop
def about(request):
    return render(request, 'about.html')

def statute(request):
    return render(request, 'statute.html')

def privacy_policy(request):
    return render(request, 'privacy.html')

def shipping(request):
    return render(request, 'shipping.html')

def returns_complaints(request):
    return render(request, 'returns.html')

def faq(request):
    return render(request, 'faq.html')

# This view allows admin user to browse all available api
@user_passes_test(lambda u: u.is_superuser)
def main_api(request):
    return render(request, 'main_api.html')
