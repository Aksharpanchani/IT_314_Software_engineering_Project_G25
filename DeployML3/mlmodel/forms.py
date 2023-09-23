from django import forms
from .models import Patient2, Patient

class PatientForm2(forms.ModelForm):
    class Meta:
              model = Patient2
              fields = "__all__"
class PatientForm(forms.ModelForm):
    class Meta:
              model = Patient
              fields = "__all__"