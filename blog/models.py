from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    Title=models.CharField(max_length=50)
    content=models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comments(models.Model):
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    auther=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.CharField(max_length=30)
    created_at=models.DateTimeField(auto_now=True)