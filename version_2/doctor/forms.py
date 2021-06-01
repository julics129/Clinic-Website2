from django import forms
from .models import appointment , contact, department, prescription
from django.forms import ModelForm, Textarea, DateTimeField 

minutes_range = range(0, 60, 5)    
minutes_choices =  [ (i, i) for i in minutes_range ]
print(minutes_choices)

gender_choices =[('male','male'),('female','female' )]
print(gender_choices)
class appointment_form(forms.ModelForm):
	PatientName = forms.CharField(label='PatientName', widget=forms.TextInput(attrs={'placeholder': 'your name','class':'form-control'}))
	PatientEmail = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'your email','class': 'form-control'})) 
	PatientPhone = forms.CharField(label='PatientPhone', widget=forms.TextInput(attrs={'placeholder': 'your phone number ','class':'form-control'}))
	Age= forms.CharField(label='Age', widget=forms.TextInput(attrs={'placeholder': 'Age ','class':'form-control'}))
	Gender=forms.ChoiceField(label='Gender', widget=forms.Select(attrs={'class': 'form-control'}))
	AppointmentDate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class':'form-control'}))
	Hour = forms.ChoiceField(label='Hour', widget=forms.Select(attrs={'class': 'form-control'}))
	Minute = forms.ChoiceField(label='Minute', widget=forms.Select(attrs={'class': 'form-control'}))
	Department = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}))
	DoctorName = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}))
	Message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'placeholder': 'your message','class':'form-control','rows':'1'}))
	#department_id = forms.ChoiceField()
	class Meta:
		model= appointment
		fields= ('PatientName','PatientEmail','PatientPhone','Message','Department','DoctorName','AppointmentDate','Hour','Minute','Age','Gender','department_id')
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['Department'].choices= [(dept.department_name, dept.department_name) for dept in department.objects.all()]
		self.fields['DoctorName'].choices=[(docnam.doctor_name, docnam.doctor_name) for docnam in department.objects.all()]
		self.fields['department_id'].choices=[(docnam.id, docnam.id) for docnam in department.objects.all()]
		self.fields['Hour'].choices=[(stime.start_time,stime.start_time) for stime in department.objects.all()]
		self.fields['Minute'].choices=minutes_choices
		self.fields['Gender'].choices=gender_choices
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

	