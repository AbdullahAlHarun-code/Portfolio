from rest_framework import serializers
from .models import (
    Category, 
    SubCategory, 
    Block)

class BlockSerializers(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = '__all__'