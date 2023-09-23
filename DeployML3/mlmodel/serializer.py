from rest_framework import serializers 
from .models import Patient2, Patient

class PatientSerializers2(serializers.ModelSerializer): 
    class meta: 
        model=Patient2
        fields='__all__'

class PatientSerializers(serializers.ModelSerializer): 
    class meta: 
        model=Patient
        fields='__all__'