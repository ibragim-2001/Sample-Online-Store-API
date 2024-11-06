from rest_framework import serializers
from .models import Categories, Products, Cart
from django.contrib.auth.models import User


class ProductsSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title', read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Categories.objects.all(), source='category', write_only=True)
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Products
        fields = ('id', 'title', 'description', 'slug',  'price', 'category', 'category_id')


class CartSerilizer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Cart
        fields = ('user', 'id', 'created')