from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(max_length=128, read_only=True)
    class Meta:
        model = Product
        fields = ['title', 'content', 'image', 'owner']
        
        # fields = '__all__'
        
    def create(self, validated_data):
    
        # context에서 올바른 request 객체를 가져옵니다.
        request = self.context.get('request')
        if request and request.user and not request.user.is_anonymous:
            validated_data['owner'] = request.user
        return super().create(validated_data)
    
