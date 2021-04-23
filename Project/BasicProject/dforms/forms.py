from django.forms import ModelForm
from .models import Student

class Studentform(ModelForm):
	class meta:
		model = Student
		fields= '__all__'