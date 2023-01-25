from django.shortcuts import render, redirect
from django.urls import reverse
from shop.models import Product
from cart.cart import Cart, Discount, Shipping, TotalPrice
from .models import OrderItem
from .forms import OrderCreateForm


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
                  'create.html',
                  {'cart': cart,
                   'form': form,
                   'discount': discount,
                   'shipping': shipping,
                   'total_price': total_price})
