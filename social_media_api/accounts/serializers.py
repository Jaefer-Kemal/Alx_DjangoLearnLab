from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        models = CustomUser
        fields = ['username', 'email', 'bio', 'profile_picture']
        
        