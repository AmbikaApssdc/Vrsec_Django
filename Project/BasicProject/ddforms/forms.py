from django import forms
from .models import Student


#class Studentform(forms.ModelForm):
#	class Meta:
#		model  = Student
#		fields = '__all__'


class Studentform(forms.ModelForm):
	class Meta:
		model  = Student
		fields = ['rollnumber','name','age','mobile','email']
		widgets={
		"rollnumber":forms.TextInput(attrs={'placeholder':"enter rollnumber",'class':"form-control"}),
		"name":forms.TextInput(attrs={'placeholder':"enter name",'class':"form-control"}),
		"age":forms.NumberInput(attrs={'placeholder':"enter age",'class':"form-control"}),
		"mobile":forms.TextInput(attrs={'placeholder':"enter mobile",'class':"form-control"}), 
		"email":forms.EmailInput(attrs={'placeholder':"enter email",'class':"form-control"})
		}

