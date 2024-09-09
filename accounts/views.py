from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import (
    api_view, permission_classes
    )
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import password_validation
from .models import User  
from .serializers import (
    SignupSerializer, ProfileSerializer, UserChangeSerializer, PasswordChangeSerializer
)
from rest_framework.permissions import IsAuthenticated

#회원가입
@api_view(["POST"])
def signup(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response({f'Welcome!{request.data["username"]}'}, status=status.HTTP_201_CREATED)


#프로필조회
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def profile(request, username):
    account = get_object_or_404(User, username=username)
    serializer = ProfileSerializer(account)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)


#선택구현
#로그아웃
@api_view(["POST"])    
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        refresh_token = request.data["refresh"]
        token = RefreshToken(refresh_token)
        token.blacklist()

        return Response({"message": "로그아웃되었습니다."}, status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response({"error": "error"}, status=status.HTTP_400_BAD_REQUEST)


#본인정보수정
@api_view(["GET", "PUT"])
@permission_classes([IsAuthenticated])
def update(request, username):
    target_user = get_object_or_404(User, username=username)
    
    if request.method == "PUT":   
        serializer = UserChangeSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        serializer = UserChangeSerializer(target_user)
        return Response(serializer.data, status=status.HTTP_200_OK)


#비밀번호변경
@api_view(["PUT"])    
@permission_classes([IsAuthenticated])
def change_password(request):
    serializer = PasswordChangeSerializer(data=request.data, context={'request':request})
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "비밀번호가 성공적으로 변경되었습니다."}, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


