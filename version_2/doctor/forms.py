from django import forms
from .models import appointment , contact, department, prescription
from django.forms import ModelForm, Textarea 



class appointment_form(forms.ModelForm):
	PatientName = forms.CharField(label='PatientName', widget=forms.TextInput(attrs={'placeholder': 'your name','class':'form-control'}))
	PatientEmail = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'your email','class': 'form-control'})) 
	PatientPhone = forms.CharField(label='PatientPhone', widget=forms.TextInput(attrs={'placeholder': 'your phone number ','class':'form-control'}))
	AppointmentDate1 = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class':'form-control'}))
	Department = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}))
	DoctorName = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}))
	Message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'placeholder': 'your message','class':'form-control','rows':'1'}))
	
	class Meta:
		model= appointment
		fields= ('PatientName','PatientEmail','PatientPhone','AppointmentDate1','Message','Department','DoctorName')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['Department'].choices= [(dept.department_name, dept.department_name) for dept in department.objects.all()]
		
		self.fields['DoctorName'].choices=[(docnam.doctor_name, docnam.doctor_name) for docnam in department.objects.all()]

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

	