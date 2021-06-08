from django.shortcuts import render
from django import forms
from .forms import appointment_form , contact_form
from .models import contact, appointment, department, prescription

import json
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, AppointmentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail


def home(request):
	formsuccess=''
	form1success=''
	form=TestForm()
	try:
		
		if request.method == 'POST':
			form = TestForm(request.POST)

			print('hi')
			#form.fields['Department'].queryset = department.objects.values_list('department_name')
						
			#appointment_form.base_fields['Department'] = forms.ModelChoiceField(queryset= department.objects.order_by('department_name').exclude())

			if form.is_valid():
				formsuccess='form_ok'
				print('form valid')
				print(request.POST.get('my_field'))
			else:
				formsuccess='form_not_ok'
				print("Form Error :\n")
				print(form.errors)
				
		else:
			
			#form.fields['dept'].queryset = department.objects.values_list('department_name')
			
			form1=TestForm(request.POST)
		return render(request, 'new.html',{'form':form, 'formsuccess':formsuccess, 'form1success':form1success})
	except Exception as e:
		print(e)
		formsuccess='Error'
		return render(request, 'new.html',{'form':form,'formsuccess':formsuccess, 'form1success':form1success})

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
				s=form.data['DoctorName']
				
				form.key_department_id = department.objects.get(doctor_name=s)
				
				id_test = department.objects.all().filter(doctor_name=s).values('id')
				print(id_test[0]['id'])
				form.save()
				name=request.POST['PatientName']
				email=request.POST['PatientEmail']
				date=request.POST['AppointmentDate']
				hour=request.POST['Hour']
				minute=request.POST['Minute']
				user=appointment.objects.create_user( 
						username=name,
						email=email
						
					)
					
				login(request,user)
				subject = 'appointment confirmation'
				message = 'hi '+{user.Name}+', your appointment booked successfully on' +{user.Date}+'.'
				email_from = settings.EMAIL_HOST_USER
				recipient_list = [user.Email,]
				send_mail(subject, message, email_from, recipient_list)
				return ("h1")
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
		date_count=appointment.objects.all().filter(AppointmentDate=date_post).count()
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
			doc_id = i.id
			doc_time = i.start_time
		data = {'d1':doc_name, 'd2':doc_id, 'd3':doc_time,}
		print(data)
		return HttpResponse(json.dumps(data))

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['GET'])
def post_collection(request):
    if request.method == 'GET':
        posts = appointment.objects.all()
        for i in posts:
            print('hi')
        print(posts)
        serializer = AppointmentSerializer(posts, many=True)
        #print(serializer)
        return Response(serializer.data)


@api_view(['GET'])
def post_element(request, pk):
    try:
        post = appointment.objects.get(pk=pk)
    except appointment.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AppointmentSerializer(post)
        return Response(serializer.data)