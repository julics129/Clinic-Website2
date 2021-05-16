from django import forms
from .models import appointment , contact, department
from django.forms import ModelForm, Textarea 

department_choices=[
	('','Department'),
	('urology','Urology'),
	('obs&gynae','Obs & Gynae'),
]
doctor_choices=[
	('','Doctors'),
	('Dr Sunita','Dr Sunita'),
	('Dr Rakesh', 'Dr Rakesh'),
]

FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]

class appointment_form(forms.ModelForm):
	PatientName = forms.CharField(label='PatientName', 
                    widget=forms.TextInput(attrs={'placeholder': 'your name','class':'form-control'}))
	PatientEmail = forms.EmailField(
    widget=forms.EmailInput(attrs={'placeholder': 'your email','class': 'form-control'})) 
	PatientPhone = forms.CharField(label='PatientPhone', 
                    widget=forms.TextInput(attrs={'placeholder': 'your phone number ','class':'form-control'}))
	AppointmentDate1 = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class':'form-control'}))
	Department = forms.ModelChoiceField(queryset=department.objects.order_by('department_name').values_list('department_name', flat=True).distinct(), empty_label='Select Department')
	# Department = forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=department_choices,attrs={'class':'form-control'}))
	Department1 = forms.ModelChoiceField(queryset=contact.objects.order_by('Email').values_list('Email', flat=True).distinct())
	DoctorName = forms.CharField(label='DoctorName',widget=forms.Select(choices=doctor_choices,attrs={'placeholder':'Doctor','class':'form-control'}))
	Message = forms.CharField(label='Message', 
                    widget=forms.Textarea(attrs={'placeholder': 'your message','class':'form-control','rows':'1'}))
	
	class Meta:
		model= appointment
		fields= "__all__"

class contact_form(forms.ModelForm):
	Name = forms.CharField(label='search', 
                    widget=forms.TextInput(attrs={'placeholder': 'your name','class':'form-control'}))
	Email = forms.EmailField(
    widget=forms.EmailInput(attrs={'placeholder': 'your email','class': 'form-control'})) 
	Subject = forms.CharField(label='search', 
                    widget=forms.TextInput(attrs={'placeholder': 'your subject','class':'form-control'}))
	Message = forms.CharField(label='search', 
                    widget=forms.Textarea(attrs={'placeholder': 'your message','class':'form-control','rows':'4'}))
	class Meta:
		model= contact
		fields="__all__"
		



