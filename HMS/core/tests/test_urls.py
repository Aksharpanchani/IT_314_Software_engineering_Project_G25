#from django.test import SimpleTestCase
#from django.urls import reverse, resolve


# # class TestUrls(SimpleTestCase):
# #     def test_homepage(self):
# #         url = reverse('login')
# #         self.assertEqual(url, '/login')





from django.test import TestCase
from django.urls import reverse

# from ..views import (
#     homepage, login, diabetesinfo, heartinfo, logout, signup,
#     dsignup, psignup, patienthome, doctorhome, predictor_diab,
#     formInfo_diab, predictor_heart, formInfo_heart, doctorreport,
#     downloadreport, homepage2
# )


class UrlsTest(TestCase):
#     def test_homepage_url(self):
#         response = self.client.get(reverse('homepage'))
#         self.assertEqual(response.status_code, 200)

#     def test_login_url(self):
#         response = self.client.get(reverse('login'))
#         self.assertEqual(response.status_code, 200)

    def test_diabetesinfo_url(self):
        response = self.client.get(reverse('diabetesinfo'))
        self.assertEqual(response.status_code, 200)

    def test_heartinfo_url(self):
        response = self.client.get(reverse('heartinfo'))
        self.assertEqual(response.status_code, 200)

#     def test_logout_url(self):
#         response = self.client.get(reverse('logout'))
#         self.assertEqual(response.status_code, 302)  # Assuming a redirect upon logout

#     def test_signup_url(self):
#         response = self.client.get(reverse('signup'))
#         self.assertEqual(response.status_code, 200)

#     def test_dsignup_url(self):
#         response = self.client.get(reverse('dsignup'))
#         self.assertEqual(response.status_code, 200)

#     def test_psignup_url(self):
#         response = self.client.get(reverse('psignup'))
#         self.assertEqual(response.status_code, 200)

#     def test_patienthome_url(self):
#         response = self.client.get(reverse('patienthome'))
#         self.assertEqual(response.status_code, 302)  # Assuming a redirect for unauthenticated users

#     def test_doctorhome_url(self):
#         response = self.client.get(reverse('doctorhome'))
#         self.assertEqual(response.status_code, 302)  # Assuming a redirect for unauthenticated users

#     #------HAS ERROR---------
#     def test_predictor_diab_url(self):
#         response = self.client.get(reverse('predictdiabetes'))
#         self.assertEqual(response.status_code, 302)  # Assuming a redirect for unauthenticated users

    # def test_formInfo_diab_url(self):
    #     response = self.client.get(reverse('resultdiabetes'))
    #     self.assertEqual(response.status_code, 302)  # Assuming a redirect for unauthenticated users

    # def test_predictor_heart_url(self):
    #     response = self.client.get(reverse('predictheart'))
    #     self.assertEqual(response.status_code, 302)  # Assuming a redirect for unauthenticated users

    # def test_formInfo_heart_url(self):
    #     response = self.client.get(reverse('resultheart'))
    #     self.assertEqual(response.status_code, 302)  # Assuming a redirect for unauthenticated users

# # ------NOW OK---
#     def test_doctorreport_url(self):
#         response = self.client.get(reverse('doctorreport'))
#         self.assertEqual(response.status_code, 302)  # Assuming a redirect for unauthenticated users

#-----eRROR
    # def test_downloadreport_url(self):
    #     response = self.client.get(reverse('downloadreport'))
    #     self.assertEqual(response.status_code, 302)  # Assuming a redirect for unauthenticated users
#--ERROR
    # def test_homepage2_url(self):
    #     response = self.client.get(reverse('homepage2'))
    #     self.assertEqual(response.status_code, 302)  # Assuming a redirect for unauthenticated users

#     # Add more test methods for other URLs as needed

# # Add more test classes if needed
# # ...
