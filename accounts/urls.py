from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [

    #회원가입, 회원탈퇴(선택구현)
    path("",views.signup),
    #로그아웃(선택구현)
    path("logout/", views.logout),
    #패스워드변경(선택구현)
    path("password/", views.change_password),
    #로그인
    path("login/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    #프로필 조회, 본인 정보 수정(선택구현)
    path("profile/<str:username>/", views.update),
    
]

