# Generated by Django 3.1.4 on 2021-05-07 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PatientName', models.CharField(max_length=30)),
                ('PatientEmail', models.EmailField(max_length=30)),
                ('PatientPhone', models.CharField(max_length=13)),
                ('AppointmentDate1', models.DateField()),
                ('Department', models.CharField(max_length=30)),
                ('DoctorName', models.CharField(max_length=30)),
                ('Message', models.CharField(max_length=70)),
            ],
        ),
    ]