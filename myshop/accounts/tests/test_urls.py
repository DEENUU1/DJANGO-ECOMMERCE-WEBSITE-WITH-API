from django.test import SimpleTestCase
from django.urls import resolve, reverse
from accounts.views import *


class TestUrls(SimpleTestCase):
    def test_signup_resolve(self):
        url = reverse("accounts:register")
        self.assertEqual(resolve(url).func.view_class, SignUpView)

    def test_signin_resolve(self):
        url = reverse("accounts:login")
        self.assertEqual(resolve(url).func.view_class, SignInView)

    def test_logout_resolve(self):
        url = reverse("accounts:logout")
        self.assertEqual(resolve(url).func.view_class, LogoutUserView)

    def test_profile_resolve(self):
        url = reverse("accounts:profile")
        self.assertEqual(resolve(url).func.view_class, ProfilView)

    def test_reset_resolve(self):
        url = reverse("accounts:reset")
        self.assertEqual(resolve(url).func.view_class, PasswordResetView)

    def test_delete_resolve(self):
        url = reverse("accounts:delete")
        self.assertEqual(resolve(url).func.view_class, DeleteUserView)
