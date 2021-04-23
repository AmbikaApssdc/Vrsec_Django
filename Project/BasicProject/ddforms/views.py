from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Studentform
from .models import Student
# Create your views here.

def add(request):
	#return HttpResponse("django")
	if request.method=="POST":
		form=Studentform(request.POST)
		if form.is_valid():
			form.save()
			#return HttpResponse("student data added successfully")
			return redirect("display")
	else:
		form=Studentform()
		return render(request,"ddforms/add.html",{'form':form})

def display(request):
	data=Student.objects.all()
	return render(request,"ddforms/display.html",{'data':data})

def edit(request,id):
	studata=Student.objects.get(id=id)
	if request.method=="POST":
		form=Studentform(request.POST,instance=studata)
		if form.is_valid():
			form.save()
			return redirect("display")
	form=Studentform(instance=studata)
	return render(request,"ddforms/edit.html",{'form':form})


def deletedata(request,id):
	studata=Student.objects.get(id=id)
	studata.delete()
	return redirect("display")

