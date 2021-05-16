from django.urls import path

from . import views

urlpatterns = [
	path('',views.home, name='home'),
	path('index',views.index, name='index'),
	path('all_appo',views.all_appo, name='all_appo'),
	path('all_contact',views.all_contact, name='all_contact'),
	path('count_appo',views.count_appo, name='count_appo'),
	path('email_count',views.email_count, name='email_count'),
	path('department_doc',views.department_doc, name='department_doc'),
]