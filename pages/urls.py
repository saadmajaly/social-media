from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home_page, name="home"),
    path("profile/<str:username>/", views.user_profile, name="profile"),
    path("profile/edit/<str:username>", views.edit_profile, name="edit_profile"),
    path("profile/save",views.save_changes, name='save'),
]
