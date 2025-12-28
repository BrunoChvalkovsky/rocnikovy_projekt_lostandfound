from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    contact = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    title = models.CharField(max_length=80)
    description = models.TextField()
    image = models.ImageField(upload_to="post_images/")
    is_solved = models.BooleanField(default=False)

    def __str__(self):
        return self.title