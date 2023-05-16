from django.urls import path
from .views import *

app_name = "accounts"

urlpatterns = [
    # This url is displaying registration form
    path("register/", SignUpView.as_view(), name="register"),
    # This url is displaying login form
    path("login/", SignInView.as_view(), name="login"),
    # This url is for logout function
    path("logout/", LogoutUserView.as_view(), name="logout"),
    # This url is displaying user profile
    path("profile/", ProfilView.as_view(), name="profile"),
    # This url is displaying password reset form
    path("reset/", PasswordResetView.as_view(), name="reset"),
    # This url is for deleting user profile
    path("delete/", DeleteUserView.as_view(), name="delete"),
]
