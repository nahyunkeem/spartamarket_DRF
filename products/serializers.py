from rest_framework import serializers
from . models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        #직렬 대상
        fields = "__all__"