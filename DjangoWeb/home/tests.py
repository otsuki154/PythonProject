from django.test import TestCase, SimpleTestCase

# Create your tests here.
class SimpleTest(SimpleTestCase):
    def testHomePageStatus(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)