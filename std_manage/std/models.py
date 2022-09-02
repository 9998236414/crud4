from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.CharField(max_length=70)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    address = models.CharField(max_length=70)
    phone = models.CharField(max_length=10)

