from rest_framework import serializers
from shop.models import Product, Category
from coupons.models import Coupon


# This serializer is for Product model
# Allows to add and get data from database
class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = Product
        fields = '__all__'


# This serializer is for Category model
# Allows to add and get data from database
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CouponsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'