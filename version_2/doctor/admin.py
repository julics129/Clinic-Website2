from django.contrib import admin
from .models import contact, appointment, department, prescription, medicines, medicines_list
from django.http import HttpResponse
from django.urls import path
from django.db import models
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.conf.urls import include, url

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from django.contrib.admin import helpers
from django.utils.html import format_html
from django.urls import reverse, reverse_lazy

class doctorContact(admin.ModelAdmin):
	list_display = ['Name','Email','Subject','Message']
	search_fields = ('Name',)
	list_filter = ('Email','Name',)
admin.site.register(contact,doctorContact)

class doctorAppointment(admin.ModelAdmin):
	list_display=('PatientName','PatientEmail','PatientPhone','AppointmentDate','Message')
	search_fields =('PatientName','PatientEmail','PatientPhone')
	list_filter = ('AppointmentDate','PatientPhone',)
admin.site.register(appointment,doctorAppointment)

class doctorDepartment(admin.ModelAdmin):
	list_display=('doctor_name','department_name',)
	search_fields=('doctor_name','department_name',)
	list_filter=('doctor_name','department_name',)
admin.site.register(department,doctorDepartment)


def my_custom_view(request):
    return HttpResponse('Admin Custom View')

class medicines_list_inline(admin.TabularInline):
    model = medicines_list
    extra = 1
    #raw_id_fields = ("medicine_name",)	
    autocomplete_fields = ['medicine_name']


class medicine_inline(admin.TabularInline):
    model = medicines
    extra = 1
    #raw_id_fields = ("medicine_name",)	

    autocomplete_fields = ['medicine_name']

class medicines_listAdmin(admin.ModelAdmin):
    list_display=('medicine_name',)
    search_fields = ('medicine_name',)
    #autocomplete_fields = ['medicine_name']

admin.site.register(medicines_list,medicines_listAdmin)

class medicinesAdmin(admin.ModelAdmin):
    list_display=('medicine_name',)
    search_fields = ('medicine_name','pres_id',)
    autocomplete_fields = ['medicine_name','pres_id']

admin.site.register(medicines,medicinesAdmin)
	
class doctorPrescription(admin.ModelAdmin):
	inlines = (medicine_inline,)
	change_form_template = 'admin/doctor/doctorPrescription/change_form2.html'
	list_display=('appointment_id','advice','print_prescriptions',)
	search_fields=('medicine','advice','appointment__PatientName')
	
	autocomplete_fields = ['appointment_id']
	
	actions = ['test_action','print_prescription']

	def my_link(self, obj):
		return format_html('<a href="%s">View on site</a>' % obj.pk)
	def get_urls(self):
		urls = super().get_urls()
		my_urls =[url(
                r'^(?P<pres_id>.+)/print_prescription/$',#'admin_action',
                self.admin_site.admin_view(self.print_prescription),
                name='print_prescription',
            ),] #[path('obj.id', self.admin_action,name='admin_action',)]
		return my_urls + urls
	def print_prescriptions(self, obj):
		return format_html(
			'<a class="button" href="{}">print prescription</a>',
			# '<a class="button" href="{}">Withdraw</a>',
            reverse('admin:print_prescription',args=[obj.pk]),
            # reverse('admin:admin_action',)
		obj)	
	def test_action(self, request, queryset):
		print(queryset)
	
	def print_prescription(self,request,pres_id, *args, **kwargs):
		print(pres_id)
		queryset=prescription.objects.all().filter(id = pres_id)
		print(queryset)
		context = {
			'title': ("Are you sure?"),
			'queryset': queryset,
			'action_checkbox_name': helpers.ACTION_CHECKBOX_NAME,
		}
		return render(request,"admin/doctor/change_form1.html",context)
	#render the default form for change or add
	def get_form(self, request, obj=None, **kwargs):
		form = super().get_form(request, obj, **kwargs)
		##form.base_fields["medicine"].label = "First Name (Humans only!):"
		return form
	
		# def get_urls(self):
		# view_name = '{}_{}_changelist'.format(
			# self.model._meta.app_label, self.model._meta.model_name)
		# return [
			# path('my_admin_path/', my_custom_view, name=view_name),
		# ]
	
	
admin.site.register(prescription,doctorPrescription)