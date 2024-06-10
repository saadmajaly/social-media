from django.urls import path
from . import views

urlpatterns = [
    path("create_post/", views.create_post, name="create_post"),
    path("create_post/save/", views.save_post, name="save_post"),
]
