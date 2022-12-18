from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Comments
from .forms import CommentForm



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


# This view represent detail of all available products
# It also displays user's comments

def main_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)

    return render(request,'detail.html',
                  {'product': product})


# This is view for adding comments
# It isn't done yet so I commented that

# def add_comment(request):
#     product = Product.objects.get()
#     form = CommentForm()
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'comments.html', context)