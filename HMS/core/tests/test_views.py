# from django.test import TestCase, Client
# from django.contrib.auth.models import User
# from ..models import PatientProfile, DoctorProfile, Report
# from django.urls import reverse
# from datetime import date

# class ViewsTestCase(TestCase):
#     def setUp(self):
#         # Create test users
#         self.patient_user = User.objects.create_user(username='testpatient', password='testpassword', email='testpatient@example.com')
#         self.doctor_user = User.objects.create_user(username='testdoctor', password='testpassword', email='testdoctor@example.com')

#         # Create test profiles
#         self.patient_profile = PatientProfile.objects.create(
#             user=self.patient_user,
#             id_user=1,
#             first_name='Test',
#             last_name='Patient',
#             height=170,
#             gender='M',
#             bloodgroup='OP',
#             birthdate=date(1990, 1, 1),
#             phone_number=1234567890
#         )
#         self.doctor_profile = DoctorProfile.objects.create(
#             user=self.doctor_user,
#             id_user=2,
#             first_name='Test',
#             last_name='Doctor',
#             phone_number=9876543210,
#             birthdate=date(1980, 1, 1),
#             gender='M',
#             speciality='MBBS',
#             work_address='Test Hospital',
#             Verified=True
#         )

#         # Create test report
#         self.test_report = Report.objects.create(
#             doctor=self.doctor_profile,
#             patient=self.patient_profile,
#             disease='TestDisease',
#             HighBP='No',
#             HighChol='No',
#             BMI=25,
#             Stroke='No',
#             HeartDiseaseAttack='No',
#             GenHlth=3,
#             Height=170,
#             Weight=70,
#             SystolicBP=120,
#             DiastolicBP=80,
#             CholestrolLevel=150,
#             GlucoseLevel=90,
#             Smoking='No',
#             PhysicalActivity='Yes',
#             Age=30,
#             Result=80,
#             DoctorConclusion=1,
#             DoctorPrescription='Take medication',
#             DoctorGeneralAdvice='Stay active'
#         )

#         # Create a test client
#         self.client = Client()

#     def test_homepage_view(self):
#         response = self.client.get(reverse('homepage'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'homepage.html')

#     def test_signup_view(self):
#         response = self.client.get(reverse('signup'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'signup.html')

#     def test_psignup_view(self):
#         response = self.client.get(reverse('psignup'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'users/patient/psignup.html')

#         # Add more tests for patient signup functionality

#     def test_dsignup_view(self):
#         response = self.client.get(reverse('dsignup'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'users/doctor/dsignup.html')

#         # Add more tests for doctor signup functionality

#     def test_login_view(self):
#         response = self.client.get(reverse('login'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'login.html')

#         # Add more tests for login functionality

#     def test_diabetesinfo_view(self):
#         response = self.client.get(reverse('diabetesinfo'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'disease/diabetes/diabetesinfo.html')

#     def test_patienthome_view(self):
#         self.client.login(username='testpatient', password='testpassword')
#         response = self.client.get(reverse('patienthome'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'users/patient/patienthome.html')

#         # Add more tests for patient home functionality

#     def test_logout_view(self):
#         self.client.login(username='testpatient', password='testpassword')
#         response = self.client.get(reverse('logout'))
#         self.assertEqual(response.status_code, 302)  # Expecting a redirect after logout

#         # Add more tests for logout functionality

#     def test_doctorhome_view(self):
#         self.client.login(username='testdoctor', password='testpassword')
#         response = self.client.get(reverse('doctorhome'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'users/doctor/doctorhome.html')

#         # Add more tests for doctor home functionality

#     def test_predictor_diab_view(self):
#         self.client.login(username='testdoctor', password='testpassword')
#         response = self.client.get(reverse('predictdiabetes'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'disease/diabetes/form_diab.html')

#         # Add more tests for diabetes predictor functionality

#     def test_formInfo_diab_view(self):
#         self.client.login(username='testdoctor', password='testpassword')
#         response = self.client.get(reverse('resultdiabetes'), {'PatientID': 'testpatient'})
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'disease/diabetes/result_diab.html')

#         # Add more tests for diabetes formInfo functionality

#     # def test_patient_report_view(self):
#     #     self.client.login(username='testpatient', password='testpassword')
#     #     response = self.client.get(reverse('patientreport'))
#     #     self.assertEqual(response.status_code, 200)
#     #     self.assertTemplateUsed(response, 'users/patient/patientreport.html')

#     #     # Add more tests for patient report functionality

#     # def test_download_report_view(self):
#     #     response = self.client.get(reverse('downloadreport'), {'report_id': self.test_report.id})
#     #     self.assertEqual(response.status_code, 200)  # Add assertions for file download

#     #     # Add more tests for download report functionality

#     # # Add more test cases for other views
