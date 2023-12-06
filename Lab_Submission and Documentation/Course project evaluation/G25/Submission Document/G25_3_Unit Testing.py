# # from django.test import TestCase
# # from django.contrib.auth import get_user_model
# # from datetime import date
# # from ..models import PatientProfile, DoctorProfile, Report

# # class ModelsTestCase(TestCase):
# #     def setUp(self):
# #         # Create a test user
# #         self.user = get_user_model().objects.create_user(
# #             username='testuser',
# #             email='testuser@example.com',
# #             password='testpassword'
# #         )

# #     def test_patient_profile_creation(self):
# #         patient_profile = PatientProfile.objects.create(
# #             user=self.user,
# #             id_user=1,
# #             first_name='John',
# #             last_name='Doe',
# #             height=175,
# #             gender='M',
# #             bloodgroup='OP',
# #             birthdate=date(1990, 1, 1),
# #             phone_number=1234567890
# #         )
# #         self.assertEqual(patient_profile.__str__(), 'testuser')

# #     def test_doctor_profile_creation(self):
# #         doctor_profile = DoctorProfile.objects.create(
# #             user=self.user,
# #             id_user=2,
# #             first_name='Dr. Jane',
# #             last_name='Smith',
# #             phone_number=9876543210,
# #             birthdate=date(1980, 1, 1),
# #             gender='F',
# #             speciality='Cardiologist',
# #             work_address='Hospital ABC',
# #             certificate='path/to/certificate.pdf',
# #             Verified=True
# #         )
# #         self.assertEqual(doctor_profile.__str__(), 'testuser')

# #     def test_report_creation(self):
# #         patient_profile = PatientProfile.objects.create(
# #             user=self.user,
# #             id_user=1,
# #             first_name='John',
# #             last_name='Doe',
# #             height=175,
# #             gender='M',
# #             bloodgroup='OP',
# #             birthdate=date(1990, 1, 1),
# #             phone_number=1234567890
# #         )

# #         doctor_profile = DoctorProfile.objects.create(
# #             user=self.user,
# #             id_user=2,
# #             first_name='Dr. Jane',
# #             last_name='Smith',
# #             phone_number=9876543210,
# #             birthdate=date(1980, 1, 1),
# #             gender='F',
# #             speciality='Cardiologist',
# #             work_address='Hospital ABC',
# #             certificate='path/to/certificate.pdf',
# #             Verified=True
# #         )

# #         report = Report.objects.create(
# #             doctor=doctor_profile,
# #             patient=patient_profile,
# #             disease='Heart Disease',
# #             HighBP='Yes',
# #             HighChol='No',
# #             BMI=25,
# #             Stroke='No',
# #             HeartDiseaseAttack='Yes',
# #             GenHlth=4,
# #             Height=180,
# #             Weight=75,
# #             SystolicBP=120,
# #             DiastolicBP=80,
# #             CholestrolLevel=200,
# #             GlucoseLevel=90,
# #             Smoking='No',
# #             PhysicalActivity='Yes',
# #             Age=30,
# #             Result=75,
# #             DoctorConclusion=1,
# #             DoctorPrescription='Take medication',
# #             DoctorGeneralAdvice='Maintain a healthy lifestyle'
# #         )

# #         self.assertEqual(report.__str__(), str(report.id))







# #-----------URL TESTING----------------



# #from django.test import SimpleTestCase
# #from django.urls import reverse, resolve


# # # class TestUrls(SimpleTestCase):
# # #     def test_homepage(self):
# # #         url = reverse('login')
# # #         self.assertEqual(url, '/login')





# from django.test import TestCase
# from django.urls import reverse

# # from ..views import (
# #     homepage, login, diabetesinfo, heartinfo, logout, signup,
# #     dsignup, psignup, patienthome, doctorhome, predictor_diab,
# #     formInfo_diab, predictor_heart, formInfo_heart, doctorreport,
# #     downloadreport, homepage2
# # )


# class UrlsTest(TestCase):
# #     def test_homepage_url(self):
# #         response = self.client.get(reverse('homepage'))
# #         self.assertEqual(response.status_code, 200)

# #     def test_login_url(self):
# #         response = self.client.get(reverse('login'))
# #         self.assertEqual(response.status_code, 200)

#     def test_diabetesinfo_url(self):
#         response = self.client.get(reverse('diabetesinfo'))
#         self.assertEqual(response.status_code, 200)

#     def test_heartinfo_url(self):
#         response = self.client.get(reverse('heartinfo'))
#         self.assertEqual(response.status_code, 200)

# #     def test_logout_url(self):
# #         response = self.client.get(reverse('logout'))
# #         self.assertEqual(response.status_code, 302)  # Assuming a redirect upon logout

# #     def test_signup_url(self):
# #         response = self.client.get(reverse('signup'))
# #         self.assertEqual(response.status_code, 200)

# #     def test_dsignup_url(self):
# #         response = self.client.get(reverse('dsignup'))
# #         self.assertEqual(response.status_code, 200)

# #     def test_psignup_url(self):
# #         response = self.client.get(reverse('psignup'))
# #         self.assertEqual(response.status_code, 200)

# #     def test_patienthome_url(self):
# #         response = self.client.get(reverse('patienthome'))
# #         self.assertEqual(response.status_code, 302)  # Assuming a redirect for unauthenticated users

# #     def test_doctorhome_url(self):
# #         response = self.client.get(reverse('doctorhome'))
# #         self.assertEqual(response.status_code, 302)  # Assuming a redirect for unauthenticated users

# #     #------HAS ERROR---------
# #     def test_predictor_diab_url(self):
# #         response = self.client.get(reverse('predictdiabetes'))
# #         self.assertEqual(response.status_code, 302)  # Assuming a redirect for unauthenticated users

#     # def test_formInfo_diab_url(self):
#     #     response = self.client.get(reverse('resultdiabetes'))
#     #     self.assertEqual(response.status_code, 302)  # Assuming a redirect for unauthenticated users

#     # def test_predictor_heart_url(self):
#     #     response = self.client.get(reverse('predictheart'))
#     #     self.assertEqual(response.status_code, 302)  # Assuming a redirect for unauthenticated users

#     # def test_formInfo_heart_url(self):
#     #     response = self.client.get(reverse('resultheart'))
#     #     self.assertEqual(response.status_code, 302)  # Assuming a redirect for unauthenticated users

# # # ------NOW OK---
# #     def test_doctorreport_url(self):
# #         response = self.client.get(reverse('doctorreport'))
# #         self.assertEqual(response.status_code, 302)  # Assuming a redirect for unauthenticated users

# #-----eRROR
#     # def test_downloadreport_url(self):
#     #     response = self.client.get(reverse('downloadreport'))
#     #     self.assertEqual(response.status_code, 302)  # Assuming a redirect for unauthenticated users
# #--ERROR
#     # def test_homepage2_url(self):
#     #     response = self.client.get(reverse('homepage2'))
#     #     self.assertEqual(response.status_code, 302)  # Assuming a redirect for unauthenticated users

# #     # Add more test methods for other URLs as needed

# # # Add more test classes if needed
# # # ...



# #--------VIEWS-------------

# import datetime
# from django.contrib.auth.models import User
# from django.test import Client, TestCase
# from django.urls import reverse
# from core.models import PatientProfile, DoctorProfile, Report

# class SignUpTests(TestCase):
#     def test_patient_signup(self):
#         response = self.client.post(reverse('psignup'), {
#             'email': 'testpatient@example.com',
#             'pass1': 'testpassword',
#             'pass2': 'testpassword',
#             'first_name': 'John',
#             'last_name': 'Doe',
#             'height': '180',
#             'gender': 'Male',
#             'bloodgroup': 'O+',
#             'birthdate': '1990-01-01',
#             'number': '1234567890',
#         })
#         self.assertEqual(response.status_code, 302)  # Check if the redirect is successful

#     def test_doctor_signup(self):
#         response = self.client.post(reverse('dsignup'), {
#             'email': 'testdoctor@example.com',
#             'pass1': 'testpassword',
#             'pass2': 'testpassword',
#             'first_name': 'Dr. Jane',
#             'last_name': 'Smith',
#             'gender': 'Female',
#             'birthdate': '1980-01-01',
#             'speciality': 'Cardiologist',
#             'work_address': 'Hospital XYZ',
#             'number': '9876543210',
#             'certificate': 'path/to/certificate.pdf',
#         })
#         self.assertEqual(response.status_code, 302)

# class LoginTests(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testpatient1', password='testpassword')

#     def test_valid_login_patient(self):
#         # Create a user and login
#         user = User.objects.create_user(username='testpatient1', password='testpassword')
#         response = self.client.post(reverse('login'), {'username': 'testpatient1', 'password': 'testpassword'})

#         # Check if the login was successful
#         self.assertEqual(response.status_code, 200)  # Check if the response is OK

#         # Check if the DoctorProfile exists for the logged-in user
#         try:
#             doctor_profile = DoctorProfile.objects.get(user=user)
#             if doctor_profile.Verified:
#                 # Your code here
#                 pass
#         except DoctorProfile.DoesNotExist:
#             # Handle the case when DoctorProfile does not exist
#             pass

#     def test_invalid_login(self):
#         response = self.client.post(reverse('login'), {'username': 'testpatient1', 'password': 'wrongpassword'})
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, reverse('login'))
#         self.assertContains(response, 'Credentials invalid')

# class PatientHomeTests(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testpatient2', password='testpassword')
#         self.patient_profile = PatientProfile.objects.create(user=self.user, first_name='John', last_name='Doe', height='170', gender='Male', bloodgroup='A+', birthdate='1995-01-01', phone_number='9876543210')

#     def test_patient_home_page(self):
#         self.client.login(username='testpatient2', password='testpassword')
#         response = self.client.get(reverse('patienthome'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'users/patient/patienthome.html')
#         self.assertContains(response, 'John Doe')


