# growbit/serializers.py
from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']  

    def create(self, validated_data):
        
        password = validated_data.pop('password')
        validated_data['password_hash'] = make_password(password)
        return User.objects.create(**validated_data)
