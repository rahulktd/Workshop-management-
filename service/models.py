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
    profilepicture = models.FileField(upload_to='documents/')


class WorkerCategory(models.Model):
    Title = models.CharField(max_length=20)

    def __str__(self):
        return self.Title
class Worker(models.Model):
    user = models.ForeignKey(Login,on_delete=models.CASCADE)
    Name = models.CharField(max_length=25)
    Address = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=20)
    profilepicture = models.FileField(upload_to='documents/')
    Work_Category = models.ForeignKey(WorkerCategory,on_delete=models.CASCADE)

class Feedback(models.Model):
    user = models.ForeignKey(Login,on_delete=models.DO_NOTHING)
    date = models.DateField(auto_now=True)
    message = models.CharField(max_length=150)
    reply = models.CharField(max_length=150, null=True, blank=True)


