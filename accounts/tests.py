from django.test import TestCase

# Create your tests here.
class AccountsRouteTests(TestCase):
    def test_login(self):

        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_signup(self):

        response = self.client.get('/signup')
        self.assertEqual(response.status_code, 301)