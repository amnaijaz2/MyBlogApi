from django.db import models
from .models import Posts,Comments
from django.contrib.auth.models import User
from rest_framework import serializers


class PostsSerializer(serializers.ModelSerializer):
     class Meta:
          model=Posts
          fields=['author','Title','content','created_at','updated_at']
          
class  CommentsSerializer(serializers.ModelSerializer):
      class Meta:
          model=Comments
          fields=['post','auther','content','created_at']
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user