from django.db import models

# Create your models here.
class appointment(models.Model):
	PatientName= models.CharField(max_length=30)
	PatientEmail= models.EmailField(max_length=30)
	PatientPhone= models.CharField(max_length=13)
	AppointmentDate1=models.DateField()
	Department=models.CharField(max_length=30)
	DoctorName=models.CharField(max_length=30)
	Message=models.CharField(max_length=70)
	
class contact(models.Model):
	Name=models.CharField(max_length=30)
	Email=models.EmailField(max_length=30)
	Subject=models.CharField(max_length=30)
	Message=models.CharField(max_length=70)
	
class department(models.Model):
	doctor_name=models.CharField(max_length=30)
	department_name=models.CharField(max_length=30)