# from django.db import models
#
# # Create your models here.
# class Login(models.Model):
#     name = models.CharField(max_length=200)
#     roll = models.CharField(max_length=10,default='S')
#     userName = models.EmailField()
#     userPassword = models.CharField(max_length=10)
#     def __str__(self):
#         fields = '__all__'
#
# class Profile(models.Model):
#     name = models.ForeignKey(id,Login)
#     profileImg = models.ImageField()
#     specilization = models.CharField()
#     course = models.CharField(default='IELTS')
#     qulification = models.CharField()
#     def __str__(self):
#         fields = '__all__'
