from django.db import models
from datetime import datetime

class department(models.Model):
	doctor_name=models.CharField(max_length=30)
	department_name=models.CharField(max_length=30)
	start_time= models.IntegerField()
	end_time = models.IntegerField()
	address=models.CharField(max_length=30)
	PhoneNumber= models.CharField(max_length=13)
	
	def __str__(self):
		return self.doctor_name+' , '+ self.department_name	

# Create your models here.
class appointment(models.Model):
	PatientName= models.CharField(max_length=30)
	PatientEmail= models.EmailField(max_length=30)
	PatientPhone= models.CharField(max_length=13)
	Age=models.IntegerField()
	Gender=models.CharField(max_length=10)
	AppointmentDate=models.DateField()
	Hour=models.IntegerField()
	Minute=models.IntegerField()
	department_id = models.ForeignKey(department, on_delete=models.CASCADE)
	# DoctorName=models.CharField(max_length=30)
	Message=models.CharField(max_length=70)

	def __str__(self):
		t = self.AppointmentDate.strftime("%d:%b:%Y:%H:%M:%p")

		return t +', '+self.PatientName.title()
	class Meta:
		#Reverse ordering in foreign key drop down in presc add
		# - is for reverse
		ordering = ['-AppointmentDate']

class contact(models.Model):
	Name=models.CharField(max_length=30)
	Email=models.EmailField(max_length=30)
	Subject=models.CharField(max_length=30)
	Message=models.CharField(max_length=70)
	

	
class prescription(models.Model):
	appointment_id = models.ForeignKey(appointment, on_delete=models.CASCADE)
	##medicine = models.CharField(max_length=30)
	advice = models.CharField(max_length=30)

class medicines_list(models.Model):
    medicine_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    compound_name = models.CharField(max_length=100)	
    def __str__(self):
        return self.medicine_name.title()+'--'+self.company_name.title()

class medicines(models.Model):
    medicine_name = models.ForeignKey(medicines_list, on_delete=models.CASCADE)
    pres_id = models.ForeignKey(prescription, on_delete=models.CASCADE)
    medicine_dose = models.CharField(max_length=100)