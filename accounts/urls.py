from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("",views.signup),
    path("logout/", views.logout),
    path("password/", views.change_passwor),
    #로그인
    path("login/", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    #프로필 조회, 본인 정보 수정(선택구현)
    path("profile/<str:username>/", views.update),
    
    
]

