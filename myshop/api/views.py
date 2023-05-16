from shop.models import Product, Category, Delivery
from coupons.models import Coupon
from order.models import Order, OrderItem
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


# This view display all available products


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]


# This view display all available category


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]


# This view display all available coupons


class CouponListView(generics.ListAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponsSerializer
    permission_classes = [IsAdminUser]


# This view display all available orders


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]


# This view display all available order items


class OrderItemListView(generics.ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAdminUser]


# This view display all available delivery options


class DeliveryListView(generics.ListAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [IsAdminUser]


# This view allows to add products


class AddProductView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]
    http_method_names = ["post", "get", "options"]


# This view allows to add category


class AddCategoryView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
    http_method_names = ["post", "get", "options"]


# This view allows to add coupon


class AddCouponView(generics.CreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponsSerializer
    permission_classes = [IsAdminUser]
    http_method_names = ["post", "get", "options"]


# This view allows to add delivery option


class AddDeliveryView(generics.CreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [IsAdminUser]
    http_method_names = ["post", "get", "options"]
