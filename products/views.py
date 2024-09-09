from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Product
from rest_framework.pagination import PageNumberPagination
from .serializers import ProductSerializer

class ProductPagination(PageNumberPagination):
    page_size = 25

class ProductListView(generics.ListAPIView):
    product = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

#상품목록조회 및 등록
@api_view(["GET", "POST"])
def product_list(request):
    if request.method == "GET":
        view = ProductListView.as_view()
        return view(request)
    
    elif request.method == "POST":
        #실제로 데이터가 들어가있는 Serializer 생성
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


#상품수정 및 삭제
@api_view(["GET", "PUT", "DELETE"])
def product_detail(request, pk):
    
    product = get_object_or_404(Product, pk=pk)
    
    if product.owner != request.users:
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