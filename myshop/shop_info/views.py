from django.shortcuts import render

# This view is to display page with information about shop
def about(request):
    return render(request, 'about.html')

def statute(request):
    return render(request, 'statute.html')

def privacy_policy(request):
    pass

def shipping(request):
    return render(request, 'shipping.html')

def returns_complaints(request):
    return render(request, 'returns.html')

def faq(request):
    return render(request, 'faq.html')

