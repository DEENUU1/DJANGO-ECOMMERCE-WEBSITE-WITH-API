import decimal
from decimal import Decimal
from django.conf import settings
from shop.models import Product, Delivery
from coupons.models import Coupon


# This class represent main cart functions
# User can add, remove, save and clear the cart
# This class also iter all items added to cart and returns the number of items


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.SESSION_COOKIE_CART)
        if not cart:
            cart = self.session[settings.SESSION_COOKIE_CART] = {}
        self.cart = cart
        self.coupon_id = self.session.get("coupon_id")

    # This method add products to cart and can change the value of them
    # At default it add 1 product to card
    # User is able to update the cart and change the quantity of items

    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {"quantity": 0, "price": str(product.price)}
        if update_quantity:
            self.cart[product_id]["quantity"] = quantity

        else:
            self.cart[product_id]["quantity"] += quantity

        self.save()

    # This method save cart in session

    def save(self):
        self.session[settings.SESSION_COOKIE_CART] = self.cart
        self.session.modified = True

    # This method allows to delete product from cart

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    # This function allows to clear all products from cart

    def clear(self):
        del self.session[settings.SESSION_COOKIE_CART]
        self.session.modified = True

    # This function iterates all products in cart

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]["product"] = product

        for item in self.cart.values():
            item["price"] = decimal.Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    # This function is counting all elements in cart
    # For example if user choose 5 times the same product the price will be the sum of them

    def __len__(self):
        return sum(item["quantity"] for item in self.cart.values())


# This class represents coupon and the value of discount after adding coupon


class Discount(object):
    def __init__(self, session):
        self.session = session
        self.coupon_id = session.get("coupon_id")

    # This function allows to add coupon
    @property
    def coupon(self):
        if self.coupon_id:
            return Coupon.objects.get(id=self.coupon_id)
        return None

    # If coupon was added to cart it will return price with this rabat
    def get_discount(self, get_total_price):
        if self.coupon:
            return (self.coupon.discount / Decimal("100")) * get_total_price
        return Decimal("0")


# This class represents value of delivery
# The administrator can change that value in admin panel
# Last added value is the price


class Shipping(object):
    def __init__(self):
        self.delivery = Delivery.objects.last()

    def shipping_value(self):
        return self.delivery.price


# This class represents total price of cart
# Method called 'get_total_price_after_discount_and_shipping' returns the final price of cart


class TotalPrice(object):
    def __init__(self, cart, discount, shipping):
        self.cart = cart
        self.discount = discount
        self.shipping = shipping

    # This function return total price of cart

    def get_total_price(self):
        return sum(item["price"] * item["quantity"] for item in self.cart)

    # This function returns total cart price after subtracted coupon rabat

    def get_total_price_after_discount(self):
        total_price = sum(item["price"] * item["quantity"] for item in self.cart)
        discount = self.discount.get_discount(total_price)
        return total_price - discount

    # This function allows to add final price
    # After coupon rabat and shipping
    # Price of shipping a constant value which is in function 'shipping_value'

    def get_total_price_after_discount_and_shipping(self):
        total_price = sum(item["price"] * item["quantity"] for item in self.cart)
        discount = self.discount.get_discount(total_price)
        shipping = self.shipping.shipping_value()
        return total_price - discount + shipping
