from django.shortcuts import render
from .models import Posts,Comments
from .serializers import PostsSerializer,CommentsSerializer,UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token





# Create your views here.
class  PostsViewset(viewsets.ModelViewSet):
     queryset=Posts.objects.all()
     serializer_class=PostsSerializer
     permission_classes=[IsAuthenticated]
     def perform_create(self, serializer):
        # Set the author to the logged-in user
        serializer.save(author=self.request.user)
    
class CommentsViewSet(viewsets.ModelViewSet):
    queryset=Comments.objects.all()
    serializer_class=CommentsSerializer
    permission_classes=[IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(auther=self.request.user)
    
class RegisterUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer  # Use the correct serializer here
    permission_classes = [AllowAny]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # Create or get token for the new user
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user).data,
            "token": token.key
        }, status=status.HTTP_201_CREATED)
    

     
    
    
