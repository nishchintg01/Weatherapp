""" Views test Module """
from django.test import TestCase
from .views import find_city_name_from_ip_addr

class YourTestClass(TestCase):
    """
    Class to Test Weather App Views Function
    """
    # @classmethod
    # def setUpTestData(cls):
    #     print("setUpTestData: Run once to set up non-modified data for all class methods.")
    #     pass

    # def setUp(self):
    #     print("setUp: Run once for every test method to set up clean data.")
    #     pass

    def test_find_ip_with_url(self):
        """
        Function to Test find_ip function with working URI
        """
        url = 'https://ipinfo.io/'
        res = find_city_name_from_ip_addr(url)
        self.assertIsInstance(res, str)

    def test_find_ip_with_none(self):
        """
        Function to Test find_ip function with URL as None
        """
        url = None
        res = find_city_name_from_ip_addr(url)
        self.assertIsNone(res)
