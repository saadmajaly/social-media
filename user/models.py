from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Follow(models.Model):
    following = models.ForeignKey(User, related_name='following_set', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='followers_set', on_delete=models.CASCADE)

class Followers(models.Model):
    user=models.ForeignKey(User, related_name='followers_count', on_delete=models.CASCADE)
    number=models.IntegerField(default=0)