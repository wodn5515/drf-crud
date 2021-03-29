from django.test import TestCase, Client

from ..models import User

import json

# Create your tests here.

client = Client()

class AccountTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="testcase", nickname="testcaseX", password="testcase")

    def test_user_create(self):
        data = {
            "username": "unittest",
            "nickname": "유닛테스트",
            "password": "dms0300!"
        }
        response = client.post("/account/register/", json.dumps(data), content_type="application/json")
        self.assertEquals(response.status_code, 201)

    def test_user_login(self):
        data = {
            "username": "testcase",
            "password": "testcase"
        }
        response = client.post("/account/login/", json.dumps(data), content_type="application/json")
        self.assertEquals(response.status_code, 201)