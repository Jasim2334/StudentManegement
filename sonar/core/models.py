from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100,blank=True)
    age = models.CharField(max_length=100,blank=True)
    roll = models.CharField(max_length=100,blank=True)
    marks = models.CharField(max_length=100,blank=True)
    gender = models.CharField(max_length=100,blank=True)
    subject = models.CharField(max_length=100,blank=True)