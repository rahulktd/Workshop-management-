from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_worker = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)

class Customer(models.Model):
    user = models.ForeignKey(Login,on_delete=models.CASCADE)
    Name = models.CharField(max_length=25)
    Address = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    # profilepicture = models.ImageField()

class Worker(models.Model):
    user = models.ForeignKey(Login,on_delete=models.CASCADE)
    Name = models.CharField(max_length=25)
    Address = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    # profilepicture = models.ImageField()