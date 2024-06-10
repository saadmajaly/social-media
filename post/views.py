from django.shortcuts import render, redirect
from .models import post
from django.contrib.auth.models import User
# Create your views here.
def create_post(request):
    
    return render(request, "create_post.html")

def save_post(request):
    content = request.POST['content']
    user=User.objects.get(username=request.user.username)
    newpost = post(content=content,user=user, likes = 0)
    newpost.save()
    return redirect("/pages/home")
