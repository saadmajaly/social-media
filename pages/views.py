from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import profile
from user.models import Followers, Follow
from post.models import post

# Create your views here.
def home_page(request):
    if User.is_authenticated:
        user_name = request.user.username
        context = {
            "owner_user_name": user_name,
        }
        return render(request, "home.html", context)
        # if the user is logged in this function will render the home page for him
    else:
        redirect("/login/")
        # will redirect the user to the login page if he is not logged in


def user_profile(request, username):
        user = User.objects.get(username=username)
        Profile = profile.objects.get(user=user)
        followers = Followers(user=user).number
        following = Follow.objects.filter(following=user).count()
        posts = post.objects.filter(user=user)
        owner = request.user == user
        owner_user_name = request.user.username
        context = {
            "user_name": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "bio": Profile.bio,
            "followers":followers,
            "following":following,
            "posts":posts,
            "owner":owner,
            "owner_user_name":owner_user_name
        }
        return render(request, "profile.html", context)

def edit_profile(request, username):
     user = User.objects.get(username=username)
     Profile = profile.objects.get(user=user)
     context = {
          "user_name": user.username,
          "first_name": user.first_name,
          "last_name": user.last_name,
          "bio": Profile.bio,
     }
     
     return render(request, "edit_profile.html", context)

def save_changes(request):
     user_name = request.POST['username']
     not_available = User.objects.filter(username=user_name).count()
     first_name=request.POST['first_name']
     last_name=request.POST['last_name']
     bio = request.POST['bio']
     context = {
          'username':user_name,
          'first_name':first_name,
          'last_name':last_name,
          'bio':bio,
          'error':''
     }
     if not_available and user_name != request.user.username:
          context['error'] = 'username already exist'
          return render(request,'edit_profile.html',context)
     else:
          user = User.objects.get(username=request.user.username)
          prof = profile.objects.get(user=user)
          user.username = user_name
          user.first_name = first_name
          user.last_name = last_name
          prof.bio = bio
          user.save()
          prof.save()
          return redirect('/pages/profile/'+user_name+'/')
