from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import contact, appointment, department, prescription

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
		
class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = appointment
        fields = ['PatientName', 'AppointmentDate','Hour']