from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import date, datetime, time

User = get_user_model()


# Create your models here.
class PatientProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    height = models.IntegerField(default=1)
    g = (('M', 'Male'), ('F', 'Female'))
    bg = (('OP', 'O +ve'), ('ON', 'O -ve'), ('AP', 'A +ve'), ('AN', 'A -ve'),
          ('BP', 'B +ve'), ('BN', 'B -ve'), ('ABP', 'AB +ve'), ('ABN', 'AB -ve'))
    gender = models.CharField(max_length=6, choices=g, default='M')
    bloodgroup = models.CharField(max_length=6, choices=bg, default='OP')
    birthdate = models.DateField(default='2003-04-16')
    phone_number = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class DoctorProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    phone_number = models.IntegerField(default=0)
    birthdate = models.DateField()
    g = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=6, choices=g, default='M')
    # bg = (('OP', 'O +ve'), ('ON', 'O -ve'), ('AP', 'A +ve'), ('AN', 'A -ve'),
    #       ('BP', 'B +ve'), ('BN', 'B -ve'), ('ABP', 'AB +ve'), ('ABN', 'AB -ve'))
    # bloodgroup = models.CharField(max_length=6, choices=bg, default='OP')
    speciality = models.TextField(default='MBBS')
    work_address = models.TextField(default='none')
    certificate = models.FileField(upload_to='certi/', default='w.pdf')
    Verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Report(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    disease = models.CharField(max_length=60)

    HighBP = models.CharField(default="-1",max_length=60)
    HighChol = models.CharField(default="-1",max_length=60)
    BMI = models.IntegerField(default=-1)
    Stroke = models.CharField(default="-1",max_length=60)
    HeartDiseaseAttack = models.CharField(default="-1",max_length=60)
    GenHlth = models.IntegerField(default=-1)

    Height = models.IntegerField(default=-1)
    Weight = models.IntegerField(default=-1)
    SystolicBP = models.IntegerField(default=-1)
    DiastolicBP = models.IntegerField(default=-1)
    CholestrolLevel = models.IntegerField(default=-1)
    GlucoseLevel = models.IntegerField(default=-1)
    Smoking = models.CharField(default="-1",max_length=60)
    PhysicalActivity = models.CharField(default="-1",max_length=60)

    Age = models.IntegerField(default=-1)
    Result = models.IntegerField(default=-1)

    DoctorConclusion = models.IntegerField(default=1)
    DoctorPrescription = models.TextField()
    DoctorGeneralAdvice = models.TextField(default='abc')

    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.id)
