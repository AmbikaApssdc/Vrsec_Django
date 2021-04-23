from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def demo(request):
	return HttpResponse('For checking Purpose...')

def hello(request):
	return HttpResponse('<h2>From Hello Function</h2>')

def stydemo(request):
	return HttpResponse("<h2 style='background-color:lightblue'>Using styles .........</h2>")

def msg(request,name):
	return HttpResponse("<h2>hii.... {} welcome </h2>".format(name))

def data(request,name,num):
	return HttpResponse("<h2> Hii .. {} your number is {} </h2>".format(name,num))

def table(request,num):
	output = ""
	for i in range(1,11):
		output += " {} X {:02} = {:02} ".format(num,i,num*i)+"<br>"
	return HttpResponse(output) 

def check(request):
	return HttpResponse('Checking Purpose')