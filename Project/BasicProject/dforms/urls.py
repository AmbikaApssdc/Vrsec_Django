from django.urls import path
from dforms import views

urlpatterns = [
	path('add/',views.addstudent),
]