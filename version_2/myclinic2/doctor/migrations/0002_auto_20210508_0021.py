# Generated by Django 3.1.4 on 2021-05-07 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='AppointmentDate1',
            field=models.DateField(auto_now=True),
        ),
    ]
