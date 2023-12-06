# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from datetime import date
# from ..models import PatientProfile, DoctorProfile, Report

# class ModelsTestCase(TestCase):
#     def setUp(self):
#         # Create a test user
#         self.user = get_user_model().objects.create_user(
#             username='testuser',
#             email='testuser@example.com',
#             password='testpassword'
#         )

#     def test_patient_profile_creation(self):
#         patient_profile = PatientProfile.objects.create(
#             user=self.user,
#             id_user=1,
#             first_name='John',
#             last_name='Doe',
#             height=175,
#             gender='M',
#             bloodgroup='OP',
#             birthdate=date(1990, 1, 1),
#             phone_number=1234567890
#         )
#         self.assertEqual(patient_profile.__str__(), 'testuser')

#     def test_doctor_profile_creation(self):
#         doctor_profile = DoctorProfile.objects.create(
#             user=self.user,
#             id_user=2,
#             first_name='Dr. Jane',
#             last_name='Smith',
#             phone_number=9876543210,
#             birthdate=date(1980, 1, 1),
#             gender='F',
#             speciality='Cardiologist',
#             work_address='Hospital ABC',
#             certificate='path/to/certificate.pdf',
#             Verified=True
#         )
#         self.assertEqual(doctor_profile.__str__(), 'testuser')

#     def test_report_creation(self):
#         patient_profile = PatientProfile.objects.create(
#             user=self.user,
#             id_user=1,
#             first_name='John',
#             last_name='Doe',
#             height=175,
#             gender='M',
#             bloodgroup='OP',
#             birthdate=date(1990, 1, 1),
#             phone_number=1234567890
#         )

#         doctor_profile = DoctorProfile.objects.create(
#             user=self.user,
#             id_user=2,
#             first_name='Dr. Jane',
#             last_name='Smith',
#             phone_number=9876543210,
#             birthdate=date(1980, 1, 1),
#             gender='F',
#             speciality='Cardiologist',
#             work_address='Hospital ABC',
#             certificate='path/to/certificate.pdf',
#             Verified=True
#         )

#         report = Report.objects.create(
#             doctor=doctor_profile,
#             patient=patient_profile,
#             disease='Heart Disease',
#             HighBP='Yes',
#             HighChol='No',
#             BMI=25,
#             Stroke='No',
#             HeartDiseaseAttack='Yes',
#             GenHlth=4,
#             Height=180,
#             Weight=75,
#             SystolicBP=120,
#             DiastolicBP=80,
#             CholestrolLevel=200,
#             GlucoseLevel=90,
#             Smoking='No',
#             PhysicalActivity='Yes',
#             Age=30,
#             Result=75,
#             DoctorConclusion=1,
#             DoctorPrescription='Take medication',
#             DoctorGeneralAdvice='Maintain a healthy lifestyle'
#         )

#         self.assertEqual(report.__str__(), str(report.id))
