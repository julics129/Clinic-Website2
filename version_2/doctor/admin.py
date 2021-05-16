from django.contrib import admin
from .models import contact, appointment, department, prescription
from django.http import HttpResponse
from django.urls import path
from django.db import models
from django.shortcuts import render
from django.template.response import TemplateResponse

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

class doctorContact(admin.ModelAdmin):
	list_display = ['Name','Email','Subject','Message']
	search_fields = ('Name',)
	list_filter = ('Email','Name',)
admin.site.register(contact,doctorContact)

class doctorAppointment(admin.ModelAdmin):
	list_display=('PatientName','PatientEmail','PatientPhone','AppointmentDate1','Department','DoctorName','Message')
	search_fields =('PatientName','Department','DoctorName', )
	list_filter = ('AppointmentDate1','Department','DoctorName','PatientPhone',)
admin.site.register(appointment,doctorAppointment)

class doctorDepartment(admin.ModelAdmin):
	list_display=('doctor_name','department_name',)
	search_fields=('doctor_name','department_name',)
	list_filter=('doctor_name','department_name',)
admin.site.register(department,doctorDepartment)

class doctorPrescription(admin.ModelAdmin):
	list_display=('medicine','advice',)
	search_fields=('medicine','advice',)
admin.site.register(prescription,doctorPrescription)