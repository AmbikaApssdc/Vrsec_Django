from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def demo(request):
	return HttpResponse('Creadted Another App')

def sample(request):
	return render(request,'SampleApp/sample.html')


def sample2(request):
	return render(request,'SampleApp/sample2.html')


def details(request,name,num):
	return render(request,'SampleApp/details.html',{'name':name,'num':num})

	
def ample2(request):
	return render(request,'SampleApp/ample.html')

def bst(request):
	return render(request,'SampleApp/bst.html')


def login(request):
	if request.method == 'POST':
		u = request.POST['uname']
		p = request.POST['pswd']
		if u == 'Ambika' and p == 'Apssdc@123':
			return HttpResponse("<h2>Hii welcome {} </h2>".format(u))
		else:
			return HttpResponse("<h2>Enter Valid Details</h2>")
	return render(request,'SampleApp/login.html')


def register(request):
	if request.method == 'POST':
		un = request.POST['uname']
		em = request.POST['email']
		mb = request.POST['mobile']
		gn = request.POST['optradio']
		dob = request.POST['dob']
		lan = request.POST.getlist('lan')
		course = request.POST['course']
		file = request.POST['file']
		comment = request.POST['txt']
		print(un,em,mb,gn,lan,course,file,comment)
		return render(request,'SampleApp/regdetails.html',{'username':un,'Email':em,'Mobile':mb,'Gender':gn,'DOB':dob,'Language':lan,'Course':course,'File':file,'Comment':comment})
	return render(request,'SampleApp/register.html')