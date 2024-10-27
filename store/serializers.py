from rest_framework import serializers
from .models import Categories, Products


class ProductsSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title', read_only=True)
    # category = serializers.PrimaryKeyRelatedField(queryset=Categories.objects.all())

    class Meta:
        model = Products
        fields = ('title', 'description', 'price', 'category')