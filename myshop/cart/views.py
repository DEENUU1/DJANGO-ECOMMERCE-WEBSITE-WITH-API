from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.urls import reverse
from shop.models import Product
from .cart import Cart
from cart.forms import CartAddProductForm
from .models import OrderItem, Order
from .forms import OrderCreateForm
from coupons.forms import CouponForm
from .tasks import order_created


# This view represents adding to cart function
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])

    return redirect('cart:cart_detail')


# This view represent remove from cart option
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


# This view represent the whole cart
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'],
                     'update': True})

    coupon_apply_form = CouponForm()

    return render(request, 'cart/detail.html',
                  {'cart': cart,
                   'coupon_apply_form': coupon_apply_form})


# This view allows user to click on the product and go back to the detail of the product
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/templates/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


# This view allows user to complete order and write all necessary information
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

            cart.clear()

            order_created.delay(order.id)

            request.session['order_id'] = order.id

            return redirect(reverse('payment:process'))

    else:
        form = OrderCreateForm()

    return render(request,
                  'cart/create.html',
                  {'cart': cart,
                   'form': form})

