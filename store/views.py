from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .models import Products, Cart
from .serializers import ProductsSerializer, CartSerilizer



class ProductsView(APIView):

    def get(self, request):
        products = Products.objects.all()

        paginator = PageNumberPagination()
        paginator.page_size = request.query_params.get('limit', 5)
        result_page = paginator.paginate_queryset(products, request)
        
        serializer = ProductsSerializer(result_page, many=True)

        for product in serializer.data:
            product['detail_url'] = f"http://127.0.0.1:8000/api/v1/products/{product['slug']}/"


        return paginator.get_paginated_response(
            {
            'data': serializer.data,
            }
        )
    

    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProductDetailView(APIView):

    def get(self, request, slug):
        product = get_object_or_404(Products, slug=slug)
        serializer = ProductsSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
  
    
    def patch(self, request, slug):
        product = get_object_or_404(Products, slug=slug)
        serializer = ProductsSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
            
    
    def delete(self, request, slug):
        product = get_object_or_404(Products, slug=slug)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class CartView(APIView):
    
    def get(self, request):
        cart = Cart.objects.get_or_create(user=request.user)
        serializer = CartSerilizer(cart, many=True)
        return Response({'data': serializer.data})