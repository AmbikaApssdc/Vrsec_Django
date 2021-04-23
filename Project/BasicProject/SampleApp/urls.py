from django.urls import path
from SampleApp import views

urlpatterns = [
	path('demo/',views.demo),
	path('sample/',views.sample),
	path('sample2/',views.sample2),
	path('details/<str:name>/<int:num>',views.details),
	path('ample2/',views.ample2),
	path('bst/',views.bst),
	path('login/',views.login),
	path('register/',views.register),
]