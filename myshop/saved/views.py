from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .saved import Saved
from .forms import SavedAddProductForm
from shop.models import Product


@require_POST
def saved_add(request, product_id):
    saved = Saved(request)
    product = get_object_or_404(Product,
                                id=product_id)
    form = SavedAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        saved.add(product=product)

    return redirect('saved:saved_detail')


def saved_remove(request, product_id):
    saved = Saved(request)
    product = get_object_or_404(Product, id=product_id)
    saved.remove(product)

    return redirect('saved:saved_detail')


def saved_detail(request):
    saved = Saved(request)

    return render(request, 'saved/detail.html', {'saved': saved})
