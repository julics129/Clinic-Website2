from django.contrib import admin

from django.http import HttpResponse
from django.urls import path
from django.db import models
from .models import contact, appointment, department
import json
# Register your models here.
@admin.register(contact)
class contact(admin.ModelAdmin):
	list_display = ("Name", "Subject","Email")
	

