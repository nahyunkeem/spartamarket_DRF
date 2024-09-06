from rest_framework import serializers
from .models import User


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "name", "nickname", "birthday", "gender", "introduce", "password")

class SigninSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "name", "nickname", "birthday")