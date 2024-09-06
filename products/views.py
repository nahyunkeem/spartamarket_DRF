from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
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
    
    elif request.method == "POST" and request.user.is_authenticated:
        #실제로 데이터가 들어가있는 Serializer 생성
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response({'error': f'로그인 해주세요'},status=status.HTTP_400_BAD_REQUEST)


#상품수정 및 삭제
@api_view(["GET", "PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def product_detail(request, pk):

    product = get_object_or_404(Product, pk=pk)
    
    if product.owner != request.user:
        return Response({'error':'수정/삭제 권한이 없습니다'}, status=status.HTTP_403_FORBIDDEN)
    
    
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