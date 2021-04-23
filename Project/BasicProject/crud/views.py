from django.shortcuts import render,redirect
from crud.models import RegDetails
from django.http import HttpResponse
# Create your views here.
def addstudent(request):
	if request.method == 'POST':
		un = request.POST.get('name')
		rn = request.POST.get('num')
		em = request.POST.get('email')
		mb = request.POST.get('mobile')
		gn = request.POST.get('optradio')
		RegDetails.objects.create(stuname=un,rollnum=rn,
							email=em,mobile=mb,gender=gn)
		return redirect('details')
		#return HttpResponse('Record inserted successfully')
	return render(request,'crud/addstudent.html')

def details(request):
	info = RegDetails.objects.all()
	return render(request,'crud/details.html',{'info':info})


def update(request,id):
	data = RegDetails.objects.get(id=id)
	if request.method == 'POST':
		data.stuname = request.POST['name']
		data.rollnum = request.POST['num']
		data.email = request.POST['email']
		data.mobile = request.POST['mobile']
		data.gender = request.POST['optradio']
		data.save()
		return redirect('details')
	return render(request,'crud/update.html',{'data':data})


#def delete(request,id):
#	obj = RegDetails.objects.get(id=id)
	if request.method == 'POST':
		obj.delete()
		return redirect('details')
	return render(request,'crud/delete.html',{'obj':obj})