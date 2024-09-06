from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import SignupSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated


#프로필조회
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def profile(request, username):
    account = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(account)
    print(serializer.data)
    return JsonResponse(serializer.data, status=200)

#회원가입
@api_view(["POST"])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({f'Welcome!{request.data["username"]}'}, status=status.HTTP_201_CREATED)
