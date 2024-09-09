from django.db import models
from accounts.models import User

class Product(models.Model):
    account = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_products')
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="static/", blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='account_products')
    
    