from rest_framework import serializers
from .models import Product
from accounts.models import User

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyFieldField(source = User.username)
    class Meta:
        model = Product
        fields = ['title', 'content', 'image', 'owner']
        
        
    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.user and not request.user.is_anonymous:
            validated_data['owner'] = request.user
        return super().create(validated_data)
    
