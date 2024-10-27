from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from .models import Products
from .serializers import ProductsSerializer


class ProductsView(APIView):

    def get(self, request):
        products = Products.objects.all()

        paginator = PageNumberPagination()
        paginator.page_size = request.query_params.get('limit', 5)
        result_page = paginator.paginate_queryset(products, request)
        
        serializer = ProductsSerializer(result_page, many=True)
        
        return paginator.get_paginated_response(
            {
            'data': serializer.data
            }
        )
    

    def post(self, request):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)