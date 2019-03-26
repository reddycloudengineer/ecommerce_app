from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('name','price','created_at','updated_at')

