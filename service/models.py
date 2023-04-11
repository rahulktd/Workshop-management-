from django.contrib.auth.models import AbstractUser
from django.db import models


class WorkerCategory(models.Model):
    Title = models.CharField(max_length=20)
    def __str__(self):
        return self.Title
# Create your models here.
class Login(AbstractUser):
    is_worker = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    name = models.CharField(max_length=25,null=True)
    address = models.CharField(max_length=100,null=True)
    mobile = models.CharField(max_length=20,null=True)
    profilepicture = models.FileField(upload_to='documents/',null=True)
    Work_Category = models.ForeignKey(WorkerCategory, on_delete=models.CASCADE,null=True)
    status = models.IntegerField(default=0,null=True)

# class Customer(models.Model):
#     user = models.ForeignKey(Login,on_delete=models.CASCADE)
#     Name = models.CharField(max_length=25)
#     Address = models.CharField(max_length=100)
#     email = models.EmailField()
#     mobile = models.CharField(max_length=20)
#     Profilepicture = models.FileField(upload_to='documents/')



# class Worker(models.Model):
#     user = models.ForeignKey(Login,on_delete=models.CASCADE, related_name="Worker")
#     Name = models.CharField(max_length=25)
#     Address = models.CharField(max_length=100)
#     email = models.EmailField()
#     mobile = models.CharField(max_length=20)
#     profilepicture = models.FileField(upload_to='documents/')
#     Work_Category = models.ForeignKey(WorkerCategory,on_delete=models.CASCADE)
#     status = models.IntegerField(default=0)

class Feedback(models.Model):
    user = models.ForeignKey(Login,on_delete=models.DO_NOTHING)
    date = models.DateField(auto_now=True)
    message = models.CharField(max_length=150)
    reply = models.CharField(max_length=150, null=True, blank=True)


