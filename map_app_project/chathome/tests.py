from django.test import TestCase
from django.urls import reverse
from . models import Userinfo

class LoginTestCase(TestCase):
    def setUp(self):
        self.user = Userinfo.objects.create_user(user_name='aaa')

    def test_login_page(self):
        login_url = reverse('login')
        response = self.client.get(login_url)
        self.assertEqual(response.status_code, 200)
        # Update the expected template name to 'registration/login.html'
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login(self):
        login_url = reverse('login')
        response = self.client.post(login_url, {'username': 'aaa@qq.com', 'password': '123456'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, expected_url=reverse(
            'indexpage'), status_code=302, target_status_code=200)

    def test_invalid_login(self):
        login_url = reverse('login')
        response = self.client.post(login_url, {
                                    'username': 'invaliduser@gmail.com', 'password': 'invalid_password'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')
        # self.assertContains(response, 'Invalid email or password')

    def test_redirect_to_register(self):
        login_url = reverse('login')
        response = self.client.get(login_url)
        self.assertContains(response, 'Register here')
        self.assertContains(response, reverse('toregister'))
