from django.db import models

# Create your models here.

class CustomUser(models.Model):
    name=models.CharField(max_length=30)
    password=models.CharField(max_length=20)

class ChatLog(models.Model):
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role=models.CharField(max_length=5)
    log=models.TextField()

