from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from pages.models import profile


# landing page
def landing_page(request):
    return render(request, "landingPage.html")


# Create your views here.
def unique_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        if User.objects.filter(username=username).exists():
            return JsonResponse({"unique": False})
        else:
            return JsonResponse({"unique": True})
    return JsonResponse({"error": "Invalid request"})


def signup(request):
    # this function will create  a new user in the database and redirect to login page after successful registration
    user_name = request.POST.get("userName")
    first_name = request.POST.get("firstName")
    last_name = request.POST.get("lastName")
    email = request.POST.get("email")
    password = request.POST.get("password")
    try:
        newu = User(
            username=user_name, first_name=first_name, last_name=last_name, email=email
        )
        newu.set_password(password)
        newu.save()
    except:
        context={
            "usern":user_name,
            "first_name":first_name,
            "last_name":last_name,
            "email":email,
            "password": password,
            "error": "User already exists",
        }
        return render(request, "signup.html", context)
    newprofile = profile(user=newu)
    newprofile.save()
    return redirect("/login/")


def loginu(request):  # this view will handle the user login process
    if request.method == "POST":
        usern = request.POST.get("userName")
        passw = request.POST.get("password")
        if usern and passw:
            if User.objects.filter(username=usern).exists():
                userr = authenticate(request, username=usern, password=passw)
                if userr is not None:
                    login(request, userr)
                    return redirect("/pages/home/")
                else:
                    return return_page(request, "invalid credentials")
    return return_page(request, "login failed")


def change_password(request):
    return


def return_page(
    request, error=""
):  # this function will return the page that contains login form
    redirect("/")
    return render(request, "login.html", {"error": error})


def return_signup(request, error=""):
    return render(request, "signup.html", {"error": error})


def logoutu(request):  # log out of account
    logout(request)
    return redirect("/")
