from django.test import TestCase
from google.oauth2 import id_token
from google.auth.transport import requests
from auth_app.models import User


class TestClass(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.idtoken = input("Testing requires a valid idtoken. Please enter it here: ")
        pass

    def setUp(self):
        pass

    def test_false_is_false(self):
        self.assertFalse(False)

    def test_false_is_true(self):
        val = input("Enter a value: ")
        print(val)
        self.assertTrue(True)

    def test_idtoken(self):
        self.assertEqual(self.idtoken, "mytoken")
    

