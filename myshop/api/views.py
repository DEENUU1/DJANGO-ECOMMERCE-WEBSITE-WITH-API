from rest_framework.response import Response
from rest_framework.decorators import api_view
from shop.models import Product, Category
from coupons.models import Coupon
from cart.models import Order, OrderItem
from .serializers import *
from django.contrib.auth.decorators import user_passes_test


''' THIS VIEWS ARE ONLY AVAILABLE FOR ADMIN USERS'''

# This view display all products info in JSON format

@user_passes_test(lambda u: u.is_superuser)
@api_view(['GET'])
def get_product_data(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# This view display all category info in JSON format

@user_passes_test(lambda u: u.is_superuser)
@api_view(['GET'])
def get_category_data(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)

# THis view allows to add products in JSON format

@user_passes_test(lambda u: u.is_superuser)
@api_view(['POST', 'GET', 'OPTIONS'])
def add_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# This view allows to add category in JSON format

@ user_passes_test(lambda u: u.is_superuser)
@api_view(['POST', 'GET', 'OPTIONS'])
def add_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# This view allows to display all available coupons in JSON format

@user_passes_test(lambda u: u.is_superuser)
@api_view(['GET'])
def get_coupon_data(request):
    coupon = Coupon.objects.all()
    serializer = CouponsSerializer(coupon, many=True)
    return Response(serializer.data)

# This view allows to add coupon in JSON format

@user_passes_test(lambda u: u.is_superuser)
@api_view(['POST', 'GET', 'OPTIONS'])
def add_coupon(request):
    serializer = CouponsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# This view allows to display customer information from order
# in JSON format

@user_passes_test(lambda u: u.is_superuser)
@api_view(['GET'])
def get_order_data(request):
    order = Order.objects.all()
    serializer = OrderSerializer(order, many=True)
    return Response(serializer.data)

# This view allows to display order information in JSON format

@user_passes_test(lambda u: u.is_superuser)
@api_view(['GET'])
def get_orderItem_data(request):
    order_item = OrderItem.objects.all()
    serializer = OrderItemSerializer(order_item, many=True)
    return Response(serializer.data)

