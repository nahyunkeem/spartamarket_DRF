from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "accounts"
urlpatterns = [

    #회원가입, 로그인, 프로필조회
    path("signup/",views.signup),
    path("signin/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("<str:username>/", views.profile)
    
    # path("logout/", views.logout, name="logout"),
    # path("password/", views.password, name="password"),
    # path("delete/",views.delete, name="delete"),
    
]

