from django.test import TestCase
from django.urls import reverse

from .models import User
from .views import is_valid_email, is_strong_password


# ------------ TDD (Test Driven Development)

class TestModel(TestCase):

    def test_user(self):
        new = User.objects.create(
            first_name='Thomas',
            last_name='Shelby',
            email='thomas@test.com',
            phone='09123456789',
            birthday='1990-01-01',
            national_id='1234567890',
            username='thomas'
        )

        the_new = User.objects.get(pk=new.id)

        self.assertEqual(the_new.first_name, 'Thomas')
        self.assertEqual(the_new.last_name, 'Shelby')
        self.assertEqual(the_new.email, 'thomas@test.com')
        self.assertEqual(the_new.phone, '09123456789')
        self.assertEqual(the_new.national_id, '1234567890')
        self.assertEqual(the_new.username, 'thomas')


class TestValidators(TestCase):

    def test_valid_email(self):
        self.assertTrue(
            is_valid_email('test@gmail.com')
        )

    def test_invalid_email(self):
        self.assertFalse(
            is_valid_email('testgmail.com')
        )

    def test_strong_password(self):
        self.assertTrue(
            is_strong_password('abc12345')
        )

    def test_weak_password(self):
        self.assertFalse(
            is_strong_password('abc')
        )


class TestView(TestCase):

    def test_register_get(self):
        response = self.client.get(
            reverse('register')
        )
        self.assertEqual(response.status_code, 200)

    def test_login_get(self):
        response = self.client.get(
            reverse('login')
        )
        self.assertEqual(response.status_code, 200)

    def test_logout_get(self):
        response = self.client.get(
            reverse('logout')
        )
        self.assertEqual(response.status_code, 200)

    def test_profile_get(self):
        response = self.client.get(
            reverse('profile')
        )
        self.assertEqual(response.status_code, 200)

    def test_register_post_empty_form(self):

        data = {
            "first_name": "",
            "last_name": "",
            "password_1": "",
            "password_2": "",
            "email": "",
            "username": "",
            "phone": "",
            "national_id": "",
            "birthday": ""
        }

        response = self.client.post(
            reverse('register'),
            data
        )

        self.assertContains(
            response,
            "Pls Fill Out The Form First!"
        )

    def test_register_post_password_mismatch(self):

        data = {
            "first_name": "Ali",
            "last_name": "Ahmadi",
            "password_1": "abc12345",
            "password_2": "abc12346",
            "email": "ali@test.com",
            "username": "ali",
            "phone": "09123456789",
            "national_id": "1234567890",
            "birthday": "2000-01-01"
        }

        response = self.client.post(
            reverse('register'),
            data
        )

        self.assertContains(
            response,
            "Two passwords do not match!"
        )

    def test_login_post(self):

        response = self.client.post(
            reverse('login'),
            {
                "email": "test@test.com",
                "password": "123456"
            }
        )

        self.assertEqual(response.status_code, 200)


class TestUrl(TestCase):

    def test_url_register(self):
        response = self.client.get(
            reverse('register')
        )
        self.assertNotEqual(response.status_code, 404)

    def test_url_login(self):
        response = self.client.get(
            reverse('login')
        )
        self.assertNotEqual(response.status_code, 404)

    def test_url_logout(self):
        response = self.client.get(
            reverse('logout')
        )
        self.assertNotEqual(response.status_code, 404)

    def test_url_profile(self):
        response = self.client.get(
            reverse('profile')
        )
        self.assertNotEqual(response.status_code, 404)
