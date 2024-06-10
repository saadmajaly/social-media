from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page),
    # will return the landing page that can route the user to the login or signup page
    path("login/", views.return_page),
    # this is the default page, when you enter social.com it will open the login and sigup page
    path("auth/", views.loginu, name="login"),
    # this url will authenticate the user and log the user in and direct the user to the home page
    path("signup/check_username_unique/", views.unique_user, name="check_username_unique"),
    # this url  is used to check if the username entered by user is already in use or not
    path("logout/", views.logoutu, name="logout"),
    path("signup/", views.return_signup),
    path("create_account/", views.signup, name="create_account"),
]
