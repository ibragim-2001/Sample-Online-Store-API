from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Products
from .serializers import ProductsSerializer


class ProductsView(APIView):

    def get(self, request):
        items = Products.objects.all()
        serializer = ProductsSerializer(items, many=True)
        return Response(serializer.data)