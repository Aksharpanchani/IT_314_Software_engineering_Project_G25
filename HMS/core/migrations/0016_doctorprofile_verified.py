# Generated by Django 4.1.5 on 2023-11-08 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_report_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorprofile',
            name='Verified',
            field=models.BooleanField(default=False),
        ),
    ]