from django.test import TestCase

# Create your tests here.

class FailingTestCase(TestCase):
    def setUp(self):
        pass

    def test_it_fails(self):
        self.assertTrue(False)
