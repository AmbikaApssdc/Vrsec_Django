from django.db import models

# Create your models here.
class Student(models.Model):
	name=models.CharField(max_length=30,default=True)
	rollnumber=models.CharField(max_length=10,default=True)
	age=models.IntegerField(default=True)
	mobile=models.CharField(max_length=10,default=True)
	email=models.EmailField(max_length=30,default=True)