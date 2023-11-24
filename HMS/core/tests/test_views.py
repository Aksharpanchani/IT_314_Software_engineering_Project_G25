
import datetime
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from core.models import PatientProfile, DoctorProfile, Report

class SignUpTests(TestCase):
    def test_patient_signup(self):
        response = self.client.post(reverse('psignup'), {
            'email': 'testpatient@example.com',
            'pass1': 'testpassword',
            'pass2': 'testpassword',
            'first_name': 'John',
            'last_name': 'Doe',
            'height': '180',
            'gender': 'Male',
            'bloodgroup': 'O+',
            'birthdate': '1990-01-01',
            'number': '1234567890',
        })
        self.assertEqual(response.status_code, 302)  # Check if the redirect is successful

    def test_doctor_signup(self):
        response = self.client.post(reverse('dsignup'), {
            'email': 'testdoctor@example.com',
            'pass1': 'testpassword',
            'pass2': 'testpassword',
            'first_name': 'Dr. Jane',
            'last_name': 'Smith',
            'gender': 'Female',
            'birthdate': '1980-01-01',
            'speciality': 'Cardiologist',
            'work_address': 'Hospital XYZ',
            'number': '9876543210',
            'certificate': 'path/to/certificate.pdf',
        })
        self.assertEqual(response.status_code, 302)

class LoginTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testpatient1', password='testpassword')

    def test_valid_login_patient(self):
        # Create a user and login
        user = User.objects.create_user(username='testpatient1', password='testpassword')
        response = self.client.post(reverse('login'), {'username': 'testpatient1', 'password': 'testpassword'})

        # Check if the login was successful
        self.assertEqual(response.status_code, 200)  # Check if the response is OK

        # Check if the DoctorProfile exists for the logged-in user
        try:
            doctor_profile = DoctorProfile.objects.get(user=user)
            if doctor_profile.Verified:
                # Your code here
                pass
        except DoctorProfile.DoesNotExist:
            # Handle the case when DoctorProfile does not exist
            pass

    def test_invalid_login(self):
        response = self.client.post(reverse('login'), {'username': 'testpatient1', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        self.assertContains(response, 'Credentials invalid')

class PatientHomeTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testpatient2', password='testpassword')
        self.patient_profile = PatientProfile.objects.create(user=self.user, first_name='John', last_name='Doe', height='170', gender='Male', bloodgroup='A+', birthdate='1995-01-01', phone_number='9876543210')

    def test_patient_home_page(self):
        self.client.login(username='testpatient2', password='testpassword')
        response = self.client.get(reverse('patienthome'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/patient/patienthome.html')
        self.assertContains(response, 'John Doe')


