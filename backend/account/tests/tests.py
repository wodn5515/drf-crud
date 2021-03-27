from django.test import TestCase

from ..models import User

# Create your tests here.

class AccountTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="testcase", nickname="testcaseX", password="testcase")

    def test_user_create(self):
        test_user = User.objects.get(username="testcase")
        self.assertEqual(test_user.nickname, "testcase")