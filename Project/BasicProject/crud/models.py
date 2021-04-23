from django.db import models

# Create your models here.
class Student(models.Model):
	rollnumber=models.CharField(max_length=10)
	name=models.CharField(max_length=30)
	age=models.IntegerField()
	#mobile=models.CharField(max_length=10)
	email=models.EmailField()


	def __str__(self):
		return self.name+' '+self.rollnumber


class RegDetails(models.Model):
	genders = [('Female','Female'),
				('Male','Male')]
	stuname = models.CharField(max_length=20)
	rollnum = models.CharField(max_length=20)
	email = models.EmailField()
	mobile = models.CharField(max_length=10)
	gender = models.CharField(max_length=10,choices=genders)

	def __str__(self):
		return self.stuname