from rest_framework import serializers
from shop.models import Product, Category, Delivery
from coupons.models import Coupon
from order.models import Order, OrderItem

# This serializer is for Product model
# Allows to add and get data from database


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = "__all__"


# This serializer is for Category model
# Allows to add and get data from database


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


# This serializer is for Coupon model
# Allows to add and get data from database


class CouponsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = "__all__"


# This serializer is for Order model
# Allows to get data from database


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


# This serializer is for OrderItem model
# Allows to get data from database


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


# This serializer is for Delivery model
# Allows to get and post data


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = "__all__"
