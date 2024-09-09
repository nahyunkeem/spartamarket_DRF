from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.pagination import PageNumberPagination


class ProductPagination(PageNumberPagination):
    page_size = 10

class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination
    
    @permission_classes([IsAuthenticated])
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user) 
            
            
#상품수정 및 삭제
@api_view(["GET", "PUT", "DELETE"])
def product_detail(request, pk):
    
    product = get_object_or_404(Product, pk=pk)
    print(product.owner, request.user)
    if product.owner != request.user:
        return Response({'error':'permisson denied'}, status=status.HTTP_403_FORBIDDEN)
    
    if request.method == "GET":
        serializer = ProductSerializer(product) 
        return Response(serializer.data)
    
    elif request.method == "PUT": 
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    elif request.method == "DELETE":
        product.delete()
        return Response({'message':'successfully deleted'},status.HTTP_204_NO_CONTENT)