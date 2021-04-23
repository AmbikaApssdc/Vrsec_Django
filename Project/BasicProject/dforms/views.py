from django.shortcuts import render
from .models import Student
from .forms import Studentform
from django.http import HttpResponse
# Create your views here.

def addstudent(request):
	if request.method=="POST":
		form=Studentform(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("student data added successfully")
	