from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # This url is displaying registration form
    path('register/', views.registerPage, name='register'),

    # This url is displaying login form
    path('login/', views.loginPage, name='login'),

    # This url is for logout function
    path('logout/', views.logoutUser, name='logout'),

    # This url is displaying user profile
    path('profile/', views.profileUser, name='profile'),

    # This url is displaying password reset form
    path('reset/', views.changePassword, name='reset'),
]