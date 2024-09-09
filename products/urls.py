from django.urls import path
from . import views


urlpatterns = [
    #상품 등록, 상품 목록 조회,
    path("", views.product_list), 
    #상품 수정, 상품 삭제
    path("<int:pk>/", views.product_detail),
    
]