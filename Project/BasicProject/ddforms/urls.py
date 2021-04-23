from django.urls import path
from ddforms import views
urlpatterns = [
	path('add/',views.add),
	path('display/',views.display,name="display"),
	path('edit/<int:id>',views.edit,name="edit"),
	path('deletedata/<int:id>',views.deletedata,name="del")
]