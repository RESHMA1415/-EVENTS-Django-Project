from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    usertype=models.CharField(max_length=50)





class User(models.Model):
    userid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    gender = models.CharField(max_length=6)
    password = models.CharField(max_length=20)

class Admin(models.Model):
    adminid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=20)

class Event(models.Model):
    eventid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField()

class Book_events(models.Model):
    bookingid = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    name = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    mobile = models.CharField(max_length=10)