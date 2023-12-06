from django.contrib import admin

# Register your models here.
from .models import PatientProfile

admin.site.register(PatientProfile)

from .models import DoctorProfile

admin.site.register(DoctorProfile)

from .models import Report

admin.site.register(Report)