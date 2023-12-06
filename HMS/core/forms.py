from django import forms
from django.utils.safestring import mark_safe

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)

BLOODGROUP_CHOICES = (('OP', 'O +ve'), ('ON', 'O -ve'), ('AP', 'A +ve'), ('AN', 'A -ve'),
          ('BP', 'B +ve'), ('BN', 'B -ve'), ('ABP', 'AB +ve'), ('ABN', 'AB -ve'))

#NOT NEEDED RIGHT NOW
# class psup(forms.Form):
#     # bloodgroup = forms.ChoiceField(choices=BLOODGROUP_CHOICES, widget=forms.Select())
#     # gender = forms.ChoiceField(label=mark_safe('<br />Gender'), choices=GENDER_CHOICES, widget=forms.RadioSelect())
#     birthdate = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
#     # phone_number = forms.IntegerField(label=mark_safe('<br />Phone Number'))

# class dsup(forms.Form):
    # bloodgroup = forms.ChoiceField(choices=BLOODGROUP_CHOICES, widget=forms.Select())
    # gender = forms.ChoiceField(label=mark_safe('<br />Gender'), choices=GENDER_CHOICES, widget=forms.RadioSelect())
    # birthdate = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    # phone_number = forms.IntegerField(label=mark_safe('<br />Phone Number'))
    # speciality = forms.CharField(widget=forms.TextInput(), label=mark_safe('<br />Speciality'))
    # work_address = forms.CharField(widget=forms.Textarea(), label=mark_safe('<br />Work Address'))
    # certificate = forms.FileField(label=mark_safe('<br/>Certificate'))
