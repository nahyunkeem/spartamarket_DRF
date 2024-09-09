from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "accounts"
urlpatterns = [

    #회원가입, 회원탈퇴
    path("",views.signup),
    #로그인
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    #프로필 조회, 본인 정보 수정
    path("<str:username>/", views.profile),
    #로그아웃
    # path("logout/", views.logout, name="logout"),
    #패스워드변경
    path("password/", views.change_password, name="password"),
    
]

