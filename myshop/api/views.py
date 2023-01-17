from rest_framework.response import Response
from rest_framework.decorators import api_view
from shop.models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render


# This view display all products info in JSON format
# Only admin user can get access to this information
@user_passes_test(lambda u: u.is_superuser)
@api_view(['GET'])
def get_product_data(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


# This view display all category info in JSON format
# Only admin user can get access to this information
@user_passes_test(lambda u: u.is_superuser)
@api_view(['GET'])
def get_category_data(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)

''' NIE DZIAŁA'''

# THis view allows to add products in JSON format
# Only admin user can get access to this function
@user_passes_test(lambda u: u.is_superuser)
@api_view(['POST'])
def add_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

''' NIE DZIAŁA'''

''' NIE DZIAŁA'''

# This view allows to add category in JSON format
# Only admin user can get access to this function
@ user_passes_test(lambda u: u.is_superuser)
@api_view(['POST'])
def add_category(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

''' NIE DZIAŁA'''

