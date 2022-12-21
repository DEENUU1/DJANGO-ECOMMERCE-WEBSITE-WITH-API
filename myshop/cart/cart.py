from decimal import Decimal
from django.conf import settings
from shop.models import Product

# This class represent all functionality of cart

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    # This function add products to cart and can change the value of them
    # At default it add 1 product to card
    # In the future the user will be able to edit that quantity in cart
    def add(self, product, quantity = 1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity

        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    # This function save cart in session
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True


    # This function allows to delete product from cart
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    # This function iterates all products in cart
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    # This function is counting all elements in cart
    # For example if user choose 5 times the same product the price will be the sum of them
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    # This function return total price of cart
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    # This function allows to clear everything from cart
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

