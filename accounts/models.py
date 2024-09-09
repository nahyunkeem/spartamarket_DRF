from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model



class User(AbstractUser):
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=10)
    nickname = models.CharField(max_length=30)
    birthday = models.DateField(auto_now_add=True)
    gender = models.CharField(max_length=2, choices=[("여","lady"),("남","gentleman")], blank=True, null=True)
    introduce = models.TextField(blank=True, null=True)
    first_name = None
    last_name = None 
