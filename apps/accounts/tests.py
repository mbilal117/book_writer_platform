from django.test import TestCase

# Create your tests here.
import json
from django.urls import path, include, reverse
from rest_framework import status
from rest_framework.test import  APITestCase, URLPatternsTestCase

from apps.accounts.models import User


class UserTests(APITestCase, URLPatternsTestCase):
    """ Test module for Users """
    urlpatterns = [
        path('api/v1/accounts/', include('apps.accounts.urls'))
    ]

    def setUp(self):
        self.user1 = User.objects.create_user(username='test2@test.com', email='test2@test.com', password='test')


    def test_login(self):
        """ Test if user can login and get token """
        url = reverse('login')
        data = {
            'username': 'test2@test.com',
            'password': 'test'
        }

        response = self.client.post(url, data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)


    def test_users(self):
        """ Test if a user can register """
        url = reverse('userList')
        data = {
            'username': 'test2@test.com',
            'password': 'test'
        }
        response = self.client.get(url, data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
