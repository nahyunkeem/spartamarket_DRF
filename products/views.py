from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer


#상품목록조회 및 등록
@api_view(["GET", "POST"])
def product_list(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
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
        return Response(status=200)