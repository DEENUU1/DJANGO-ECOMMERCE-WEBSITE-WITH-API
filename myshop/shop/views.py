from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductRate
from cart.forms import CartAddProductForm
from .forms import RateForm
from django.template import loader
from django.http import HttpResponse
from django.db.models import Avg
from django.db.models import Q
from .filters import ProductFilter, RateFilter
from django.core.paginator import Paginator


# This view represent all products
# The view displays only available products
def product_list(request, category_slug=None):
    category = None

    # Set up filter

    product_filter = ProductFilter(
        request.GET, queryset=Product.objects.filter(available=True)
    )

    cart_product_form = CartAddProductForm()

    # Set up Pagination

    p = Paginator(product_filter.qs, 9)
    page = request.GET.get("page")
    products_list = p.get_page(page)

    return render(
        request,
        "shop/products/product_list.html",
        {
            "category": category,
            "form": product_filter.form,
            "cart_product_form": cart_product_form,
            "products_list": products_list,
        },
    )


# This view represent detail of all available products
# It also displays user's comments and rates
# User can filter product's rates by the value of rate from 1 to 5


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    cart_product_form = CartAddProductForm()

    # Set up filters
    rate_filter = RateFilter(
        request.GET, queryset=ProductRate.objects.filter(product=product)
    )

    # It displays all rates sorted by dates
    # rates is only used for average_rating
    rates = ProductRate.objects.filter(product=product).order_by("date")

    # It allows to display avg of all rates
    average_rating = rates.aggregate(Avg("rate"))

    return render(
        request,
        "shop/products/product_detail.html",
        {
            "product": product,
            "cart_product_form": cart_product_form,
            "rate_filter": rate_filter,
            "average_rating": average_rating,
        },
    )


# This view is representing product rate


def product_rate(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    if request.method == "POST":
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.product = product
            rate.save()
            return redirect("shop:product_detail", id=id, slug=slug)

    else:
        form = RateForm()

    template = loader.get_template("shop/products/product_rate.html")

    context = {
        "form": form,
        "product": product,
    }

    return HttpResponse(template.render(context, request))


# This view is to display search bar
# And search result
# It searching products by the name and product's tags


def search(request):
    query = request.GET.get("q")
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(tag__icontains=query)
        ).filter(available=True)
    else:
        products = Product.objects.none()
    return render(request, "shop/products/product_search.html", {"products": products})
