from django.db import models

# Create your models here.
class Student(models.Model):
	name=models.CharField(max_length=30),
	rollnumber=models.CharField(max_length=10),
	age=models.IntegerField(),
	mobile=models.CharField(max_length=10),
	email=models.EmailField(max_length=30)