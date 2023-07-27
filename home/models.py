from django.db import models

# Create your models here.
class Login(models.Model):
    name = models.CharField(max_length=200)
    roll = models.CharField(max_length=10,default='S')
    userName = models.EmailField()
    userPassword = models.CharField(max_length=10)
    # def __str__(self):
    #     fields = '__all__'

class Profile(models.Model):
    name = models.ForeignKey(Login,on_delete=models.CASCADE,related_name='Profile')
    profileImg = models.ImageField()
    specilization = models.CharField(max_length=200)
    course = models.CharField(max_length=200,default='IELTS')
    qulification = models.CharField(max_length=200)
    # def __str__(self):
    #     fields = '__all__'
