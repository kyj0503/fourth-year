from django.db import models

# Create your models here.
class Student(models.Model):
    age = models.IntegerField()
    birthday = models.DateField()
    grade = models.IntegerField()
    major = models.CharField(max_length=50)

class Hacsam(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    stdnum = models.IntegerField()
    major = models.CharField(max_length=50)
    email = models.EmailField()

