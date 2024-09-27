from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=10)
    nickname = models.CharField(max_length=30)
    birthday = models.DateField(auto_now=True)
    
    gender_choices = [("m", "남성"),("f","여성")]
    gender = models.CharField(max_length=1, choices=gender_choices)
    gender = models.CharField(max_length=1, choices=[("1","lady"),("0","gentleman")], blank=True, null=True)
    
    introduce = models.TextField(blank=True, null=True)
    first_name = None
    last_name = None 


    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True    
    )

    def __str__(self):
        return self.username
