from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class post(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes_counter = models.IntegerField(default=0)
    comments_counter = models.IntegerField(default=0)

class Like(models.Model):
    post = models.ForeignKey(post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

