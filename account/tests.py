from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import UserProfile


# test the user registration endpoint
class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data = {"username": "nikita", "password": "PASwwordLit", "email": "nikita@gmail.com"}
        response = self.client.post('/auth/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# test case for the userprofile model
class UserProfileTestCase(APITestCase):
    profile_list_url = reverse('all-profiles')

    def setUp(self):
        # create new user and send request for endpoint in djoser
        self.user = self.client.post('/auth/users/', data={'username': 'mario', 'password': 'i-keep-jumping'})
        # take token from  new user
        response = self.client.post('/auth/jwt/create/', data={'username': 'mario', 'password': 'i-keep-jumping'})
        self.token = response.data['access']
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    # take list of all users profile in auth of user
    def test_userprofile_list_authenticated(self):
        response = self.client.get(self.profile_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    # take list of all users profile when request of user not finish yet check of permission
    def test_userprofile_list_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.profile_list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # проверьте, чтобы получить данные профиля аутентифицированного пользователя
    def test_userprofile_detail_retrieve(self):
        response = self.client.get(reverse('profile', kwargs={'pk': 1}))
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # заполнить профиль пользователя, который был автоматически создан с использованием сигналов
    def test_userprofile_profile(self):
        profile_data = {'description': 'I am a very famous game character', 'location': 'nintendo world',
                        'is_creator': 'true', }
        response = self.client.put(reverse('profile', kwargs={'pk': 1}), data=profile_data)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
