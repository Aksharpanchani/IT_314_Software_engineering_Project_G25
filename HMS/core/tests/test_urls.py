from django.test import SimpleTestCase
from django.urls import reverse, resolve


class TestUrls(SimpleTestCase):
    def test_homepage(self):
        url = reverse('login')
        self.assertEqual(url, '/login')