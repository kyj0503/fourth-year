from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hacsam(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    stdnum = models.IntegerField()
    major = models.CharField(max_length=50)
    email = models.EmailField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

