# Generated by Django 3.1.4 on 2021-05-18 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='Hour',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='Minute',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='department',
            name='end_time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='department',
            name='start_time',
            field=models.IntegerField(),
        ),
    ]