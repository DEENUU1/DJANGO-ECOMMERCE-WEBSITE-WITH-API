from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.urls import reverse
from shop.models import Product
from .cart import Cart, Discount, Shipping, TotalPrice
from cart.forms import CartAddProductForm
from .models import OrderItem
from .forms import OrderCreateForm
from coupons.forms import CouponForm


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
    discount = Discount(request.session)
    shipping = Shipping()
    total_price = TotalPrice(cart, discount, shipping)
    coupon_discount = discount.get_discount(total_price.get_total_price())

    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'],
                     'update': True})

    coupon_apply_form = CouponForm()

    return render(request, 'cart/detail.html',
        {'cart': cart,
        'coupon_apply_form': coupon_apply_form,
         'discount': discount,
         'shipping': shipping,
         'total_price': total_price,
         'coupon_discount': coupon_discount})


# This view allows user to complete order and write all necessary information

def order_create(request):
    cart = Cart(request)
    discount = Discount(request.session)
    shipping = Shipping()
    total_price = TotalPrice(cart, discount, shipping)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_price = total_price.get_total_price_after_discount_and_shipping()

            if discount.coupon:
                order.coupon = discount.coupon
                order.discount = discount.coupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])

                product = Product.objects.get(id=item['product'].id)
                product.stock -= item['quantity']
                product.save()

                if product.stock == 0:
                    product.available = False
                    product.save()

            cart.clear()

            request.session['order_id'] = order.id

            return redirect(reverse('payment:process'))

    else:
        form = OrderCreateForm()

    return render(request,
                  'cart/create.html',
                  {'cart': cart,
                   'form': form,
                   'discount': discount,
                   'shipping': shipping,
                   'total_price': total_price})
