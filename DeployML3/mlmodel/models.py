from django.db import models

# Create your models here.
class Patient2(models.Model):
    GENDER_CHOICES = (('Male','Male'),('Female', 'Female') )
    # HighBP = models.BooleanField()
    # HighChol = models.BooleanField()
    # HeartDiseaseorAttack = models.IntegerField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    age = models.IntegerField()
    salary = models.IntegerField()
    def __str__(self):
            return self.gender
    

class Patient(models.Model):
    GENDER_CHOICES = (('Male','Male'),('Female', 'Female') )
    HighBP = models.BooleanField()
    HighChol = models.BooleanField()
    HeartDiseaseorAttack = models.BooleanField()
    BMI = models.FloatField()
    Income = models.FloatField()
    GenHlth = models.FloatField()
    Age = models.IntegerField()
    def __str__(self):
            return self.gender
