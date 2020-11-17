from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="blog_like")
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title