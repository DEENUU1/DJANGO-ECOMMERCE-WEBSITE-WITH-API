from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.forms import CartAddProductForm
from .forms import RateForm

# This view represent all products
# The view displays only available products
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/products/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


# This view represent detail of all available products
# It also displays user's comments

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,'shop/products/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})



# This view is representing product rate

# def product_rate(request):
#     product = Product.objects.get()
#
#     if request.method == 'POST':
#         form = RateForm(request.POST)
#         if form.is_valid():
#             rate = form.save(commit=False)
#             rate.movie = product
#             rate.save()
#             return render(request, 'shop/products/detail.html',
#                           {'product': product})
#
#     else:
#         form = RateForm()
#
#     template = loader.get_template(;)

