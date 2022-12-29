from django.shortcuts import render, get_object_or_404
from .models import Product, Category, ProductRate
from cart.forms import CartAddProductForm
from .forms import RateForm, ProductsFilterForm
from django.template import loader
from django.http import HttpResponse
from django.db.models import Avg
from django.db.models import Q
from .filters import ProductFilter
from django.core.paginator import Paginator


# This view represent all products
# The view displays only available products
def product_list(request):
    category = None

    # Set up filter

    product_filter = ProductFilter(request.GET, queryset=Product.objects.filter(available=True))

    # Set up Pagination

    p = Paginator(product_filter.qs, 2)
    page = request.GET.get('page')
    products_list = p.get_page(page)

    return render(request, 'shop/products/list.html',
                  {'category': category,
                   'form': product_filter.form,
                   'products_list': products_list})


# This view represent detail of all available products
# It also displays user's comments

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()

    # It displays all rates sorted by dates
    rates = ProductRate.objects.filter(product=product).order_by('date')

    # It allows to display avg of all rates
    average_rating = rates.aggregate(Avg('rate'))

    return render(request, 'shop/products/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'rates': rates,
                   'average_rating': average_rating})


# This view is representing product rate

def product_rate(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)

    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.product = product
            rate.save()
            return render(request, 'shop/products/detail.html',
                          {'product': product})

    else:
        form = RateForm()

    template = loader.get_template('shop/products/rate.html')

    context = {
        'form': form,
        'product': product,
    }

    return HttpResponse(template.render(context, request))


# This view is to display page with information about shop
def about_us(request):
    return render(request, 'shop/about.html')


# This view is to display search bar
# And search result
# It searching products by the name and description

def search(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        ).filter(available=True)
    else:
        products = Product.objects.none()
    return render(request, 'shop/products/search.html', {'products': products})
