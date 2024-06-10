from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import profile


# Create your views here.
def home_page(request):
    if User.is_authenticated:
        user_name = request.user.username
        context = {
            "user_name": user_name,
        }
        return render(request, "home.html", context)
        # if the user is logged in this function will render the home page for him
    else:
        redirect("/login/")
        # will redirect the user to the login page if he is not logged in


def user_profile(request, username):
    if request.user.username == username:
        user_profile = profile.objects.get(user=request.user)
        context = {
            "user_name": request.user.username,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "bio": user_profile.bio,
        }
        return render(request, "profile.html", context)
