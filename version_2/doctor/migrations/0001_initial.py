# Generated by Django 3.1.4 on 2021-05-16 12:28

from django.db import migrations, models
import django.db.models.deletion


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
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.EmailField(max_length=30)),
                ('Subject', models.CharField(max_length=30)),
                ('Message', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=30)),
                ('department_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='prescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine', models.CharField(max_length=30)),
                ('advice', models.CharField(max_length=30)),
                ('appointment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.appointment')),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.department')),
            ],
        ),
    ]