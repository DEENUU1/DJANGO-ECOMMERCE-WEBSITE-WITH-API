from django.db import models
from shop.models import Product
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from coupons.models import Coupon
from cart.cart import Shipping

# This model allows user to write all necessary information
# All fields are required to complete the form


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    # This button is only visible in admin panel
    # Admin can see and set the order status
    # On default the order status is set to 'nowe' (1)

    coupon = models.ForeignKey(
        Coupon, related_name="orders", null=True, blank=True, on_delete=models.CASCADE
    )
    discount = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    ORDER_STATUS = [
        (1, "nowe"),
        (2, "w realizacji"),
        (3, "wysłane"),
        (4, "odebrane"),
        (5, "anulowane"),
        (6, "zwrócone"),
    ]

    order_status = models.PositiveIntegerField(choices=ORDER_STATUS, default=1)

    def get_total_cost(self, request):
        total_cost = sum(item.get_cost() for item in self.items.all())
        shipping = Shipping()
        shipping_price = shipping.shipping_value()
        return (
            shipping_price + total_cost - total_cost * (self.discount / Decimal("100"))
        )

    def __str__(self):
        return "Order {}".format(self.id)

    class Meta:
        ordering = ("-created",)


# This model allows website to save users order


class OrderItem(models.Model):
    objects = None
    object = None
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)

    product = models.ForeignKey(
        Product, related_name="order_items", on_delete=models.CASCADE
    )

    price = models.DecimalField(max_digits=10, decimal_places=2)

    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return "{}".format(self.id)

    def get_cost(self):
        return self.price * self.quantity
