from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    birth_date = models.DateField()
    grade = models.CharField(max_length=10)  # 성적 (A+, A, B+ 등)
    subject = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name 