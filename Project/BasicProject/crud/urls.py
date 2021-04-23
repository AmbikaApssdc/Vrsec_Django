from django.urls import path
from crud import views

urlpatterns = [
	path('addstudent/',views.addstudent,name='addstudent'),
	path('details/',views.details,name='details'),
	path('update/<int:id>/',views.update,name ='update'),
	#path('delete/<int:id>/',views.delete,name='delete'),
]
