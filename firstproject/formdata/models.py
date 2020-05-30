from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    branch = models.CharField(max_length=20) 

class userdetails(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    phone_number = models.IntegerField(default=0)
    city = models.CharField(max_length=30,default="none")
    state = models.CharField(max_length=30,default="none")


