from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.CharField(max_length=100, default="GUEST")
    title = models.CharField(max_length=200, default="제목없음")
    description = models.TextField(default="내용없음")
    created_date = models.DateTimeField(
            default=timezone.now)
    path = models.FileField(upload_to="img", null=False, default="../static/img/no_image.jpg")

    def __str__(self):
        return self.title
