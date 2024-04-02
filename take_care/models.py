from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    owner_name = models.CharField(max_length=100)
    pet_name = models.CharField(max_length=100)
    pet_category = models.CharField(max_length=100)
    pet_age = models.IntegerField()
    pet_description = models.TextField()
    pet_address = models.TextField()
    pet_image_url = models.URLField(max_length=200)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts_created')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Saved(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="saved_posts")
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="saved_owners")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Interested(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="interested_posts")
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="interested_owners")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
