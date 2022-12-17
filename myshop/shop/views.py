from django.shortcuts import render, get_object_or_404
from .models import Product, Category




# This view represent all products
# The view displays only available products
def main(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'index.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})

