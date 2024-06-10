from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home_page, name="home"),
    path("profile/<str:username>/", views.user_profile, name="profile"),
]
