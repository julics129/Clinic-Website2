from django.shortcuts import render
from django import forms
from .forms import appointment_form , contact_form
from .models import contact, appointment, department
import json

# Create your views here.
from django.http import HttpResponse


def home(request):
	return render(request, 'new.html')

def index(request):
	formsuccess=''
	form1success=''
	try:
		if request.method == 'POST':
			print('hi')
			form=appointment_form(request.POST)
			form1=contact_form(request.POST)
			if form.is_valid():
				formsuccess='form_ok'
				print('form valid')
				form.save()
			else:
				formsuccess='form_not_ok'
				print("Form Error :\n")
				print(form.errors)
				
			if form1.is_valid():
				name_post = request.POST['Name']
				print(name_post)
				allob = contact.objects.all().filter(Name=name_post).count()
				print(allob)
				
				if allob == 0:
					form1success='form1_ok'
					print('form1 valid')
					form1.save()
				else:
					form1success='Repeat_user'
			else:
				form1success='form1_not_ok'
				print("Form1 Error :\n")
				print(form1.errors)
		else:
			print('h1')
			form = appointment_form()
			form1=contact_form()
		return render(request, 'index.html',{'form':appointment_form,'form1':contact_form, 'formsuccess':formsuccess, 'form1success':form1success})
	except Exception as e:
		print(e)
		formsuccess='Error'
		return render(request, 'index.html',{'form':appointment_form,'form1':contact_form,'formsuccess':formsuccess, 'form1success':form1success})

def all_contact(request):
	allob = contact.objects.all()
	for i in allob:
		print(i.Name)
	return render(request, 'data_retrive_contact.html',{'allob':allob})

def all_appo(request):
	AllAppo = appointment.objects.all()
	for i in AllAppo:
		print(i)
	return render(request, 'data_retrive_appo.html', {'AllAppo':AllAppo})

def count_appo(request):
	if request.method == 'GET':
		date_post = request.GET['app_date']
		print(date_post)
		date_count=appointment.objects.all().filter(AppointmentDate1=date_post).count()
		print('date')
		j='test data'
		print(date_count)
		data = {'d1':date_count,'d2':j}
		return HttpResponse(json.dumps(data))
		
def email_count(request):
	print('hello')
	if request.method == 'GET':
		email_1 = request.GET['cont_email']
		print('new')
		print(email_1)
		email_count1=contact.objects.all().filter(Email=email_1).count()
		print(email_count1)
		data = {'d1':email_count1, }
		print('hehehe')
		return HttpResponse(json.dumps(data))

def department_doc(request):
	if request.method == 'GET':
		dep_post = request.GET['dep_name']
		print(dep_post)
		print('h8')
		dep_data = department.objects.all().filter(department_name=dep_post)
		
		for i in dep_data:
			print(i.doctor_name)
			doc_name = i.doctor_name
		data = {'d1':doc_name,}
		print(data)
		return HttpResponse(json.dumps(data))