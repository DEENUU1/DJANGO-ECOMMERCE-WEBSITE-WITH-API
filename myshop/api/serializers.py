from rest_framework import serializers
from shop.models import Product, Category


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
    name = serializers.CharField(max_length=200)
    slug = serializers.SlugField(max_length=200)
    class Meta:
        model = Category
        fields = '__all__'
